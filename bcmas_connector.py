# --
# File: bcmas_connector.py
#
# Copyright (c) Phantom Cyber Corporation, 2017-2018
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber.
#
# --

# Phantom App imports
import phantom.app as phantom
from phantom.vault import Vault
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector

# Imports local to this App
from bcmas_consts import *

from lxml import etree
import simplejson as json
import requests
import time


# Define the App Class
class BCMASConnector(BaseConnector):

    ACTION_ID_TEST_CONNECTIVITY = "test_connectivity"
    ACTION_ID_DETONATE_FILE = "detonate_file"
    ACTION_ID_GET_REPORT = "get_report"

    def __init__(self):

        # Call the BaseConnectors init first
        super(BCMASConnector, self).__init__()

        self._base_url = None
        self._api_key = None

    def initialize(self):

        config_url = self.get_config().get('url', '')
        config_url += '' if config_url.endswith('/') else '/'

        self._base_url = config_url + 'rapi/'

        return phantom.APP_SUCCESS

    def finalize(self):

        return phantom.APP_SUCCESS

    def _make_rest_call(self, action_result, endpoint, body={}, files={}, method=requests.post, add_data=True):

        config = self.get_config()

        try:
            response = method(self._base_url + endpoint,
                    params={'token': self._api_key},
                    data=body,
                    files=files,
                    verify=config.get('verify_server_cert', True))

            text = response.text

            if (text.startswith('<html>')):

                if response.status_code == 401:
                    return (action_result.set_status(phantom.APP_ERROR, "Configured credentials are not valid"), None)

                if response.status_code == 404:
                    return (action_result.set_status(phantom.APP_ERROR, "Could not find required resource via the API"), None)

                xml = etree.fromstring(text)
                return (action_result.set_status(phantom.APP_ERROR, xml.find('title').text), None)

            resp_json = response.json()

        except Exception as e:
            return (action_result.set_status(phantom.APP_ERROR, BCMAS_ERR_SERVER_CONNECTION, e), None)

        if (response.status_code != 200):

            if add_data:
                action_result.add_data(resp_json)

            return (action_result.set_status(phantom.APP_ERROR, BCMAS_ERR_FROM_SERVER), None)

        return phantom.APP_SUCCESS, resp_json

    def _set_api_key(self, action_result):

        config = self.get_config()

        key = config.get('api_key')

        if key:
            self._api_key = key
            return phantom.APP_SUCCESS

        username = config.get('username')
        password = config.get('password')

        if (not (username and password)):
            return action_result.set_status(phantom.APP_ERROR, "Asset not configured correctly, need either username and password or API key")

        params = {'username': username, 'password': password}

        try:
            response = requests.post(self._base_url + 'auth/session',
                    data=params,
                    verify=config.get('verify_server_cert', True))

            if response.status_code == 401:
                return action_result.set_status(phantom.APP_ERROR, "Configured username and password are not valid")

            resp_json = response.json()

        except Exception as e:
            return (action_result.set_status(phantom.APP_ERROR, BCMAS_ERR_SERVER_CONNECTION, e))

        key = resp_json.get('results', {}).get('session_token_string')

        if (not key):
            return action_result.set_status(phantom.APP_ERROR, "Configured username and password are not valid")

        self._api_key = key

        return phantom.APP_SUCCESS

    def _test_connectivity(self, param):

        action_result = self.add_action_result(ActionResult(dict(param)))

        if (not self._set_api_key(action_result)):
            self.save_progress(action_result.get_message())
            return action_result.set_status(phantom.APP_ERROR, "Test connectivity failed")

        ret_val, resp_json = self._make_rest_call(action_result, 'auth/sessions', method=requests.get)

        if (not ret_val):
            self.save_progress(action_result.get_message())
            return action_result.set_status(phantom.APP_ERROR, "Test connectivity failed")

        if ('GET /auth/sessions' != resp_json.get('request')):
            self.save_progress(BCMAS_ERR_FROM_SERVER)
            return action_result.set_status(phantom.APP_ERROR, "Test connectivity failed")

        action_result.add_data(resp_json)

        self.save_progress("Test Connectivity Passed")

        return action_result.set_status(phantom.APP_SUCCESS)

    def _create_sample(self, action_result, param, body):

        vault_id = param.get('vault_id', '')

        # check the vault for a file with the supplied ID
        file_path = Vault.get_file_path(vault_id)

        if (not file_path):
            return action_result.set_status(phantom.APP_ERROR, BCMAS_ERR_NOT_IN_VAULT)

        upfile = open(file_path, 'rb')

        username = param.get('owner', self.get_config().get('username'))

        params = {}

        if (not username):
            return action_result.set_status(phantom.APP_ERROR, "No owner could be set. Either set the owner parameter for the action, or the username parameter for the asset.")

        params['owner'] = username

        description = param.get('description')
        if description:
            params['description'] = description

        source = param.get('source')
        if source:
            params['source'] = source

        label = param.get('label')
        if label:
            params['label'] = label

        ret_val, resp_json = self._make_rest_call(action_result, 'samples/basic', body=params, files={'file': upfile})

        if (not ret_val):
            return phantom.APP_ERROR

        sample_id = resp_json.get('results', [{}])[0].get('samples_sample_id')

        if (not sample_id):
            return action_result.set_status(phantom.APP_ERROR, "Could not get sample ID after upload")

        body['sample_id'] = sample_id

        return phantom.APP_SUCCESS

    def _create_task(self, action_result, param, body):

        environment = BCMAS_ENV_DICT.get(param.get('environment', 'IntelliVM'), 'ivm')

        body['env'] = environment
        body['priority'] = param.get('priority', 'high')

        profile = param.get('profile')

        if (environment == 'ivm') and profile:

            try:
                int(profile)
                body['vmp_id'] = profile

            except:
                body['ivm_profile'] = profile

        ret_val, resp_json = self._make_rest_call(action_result, 'tasks', body=body)

        if (not ret_val):
            return phantom.APP_ERROR, None

        task_id = resp_json.get('results', [{}])[0].get('tasks_task_id')

        if (not task_id):
            return action_result.set_status(phantom.APP_ERROR, "Could not start task on uploaded sample"), None

        return phantom.APP_SUCCESS, task_id

    def _wait_for_task_complete(self, action_result, task_id):

        max_wait = self.get_config().get('timeout')

        if (max_wait is None):
            max_wait = BCMAS_MAX_TIMEOUT_DEF

        max_attempts = ((int(max_wait) * 60) / BCMAS_SLEEP_SECS) if (int(max_wait) != 0) else 1

        num_attempts = 0

        while num_attempts < max_attempts:

            ret_val, resp_json = self._make_rest_call(action_result, 'tasks/{}'.format(task_id), method=requests.get)

            if (ret_val) and (resp_json.get('results', [{}])[0].get('task_state_state', '') in BCMAS_TASK_COMPLETE_LIST):
                action_result.add_data(resp_json)
                return action_result.set_status(phantom.APP_SUCCESS, "Detonation successfully completed on uploaded file")

            if ('not find' in action_result.get_message()):
                return action_result.set_status(phantom.APP_ERROR, "Could not create a task for uploaded sample")

            num_attempts += 1
            time.sleep(BCMAS_SLEEP_SECS)

        action_result.add_data(resp_json if resp_json is not None else {})

        return action_result.set_status(phantom.APP_SUCCESS, BCMAS_MSG_MAX_POLLS_REACHED)

    def _detonate_file(self, param):

        self.debug_print("param", param)

        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        self._set_api_key(action_result)

        body = {}

        if (not self._create_sample(action_result, param, body)):
            return phantom.APP_ERROR

        ret_val, task_id = self._create_task(action_result, param, body=body)

        if (not ret_val):
            return phantom.APP_ERROR

        if (not self._wait_for_task_complete(action_result, task_id)):
            return phantom.APP_ERROR

        resp_json = action_result.get_data()[0]

        summary = {}
        summary['task_status'] = resp_json.get('results', [{}])[0].get('task_state_state', 'UNKNOWN_STATE')
        summary['risk_score'] = resp_json.get('results', [{}])[0].get('tasks_owner_risk_score', 'UNKNOWN_STATE')
        action_result.set_summary(summary)

        return phantom.APP_SUCCESS

    def _get_report(self, param):

        action_result = self.add_action_result(ActionResult(dict(param)))

        self._set_api_key(action_result)

        task_id = param.get('task_id')

        ret_val, resp_json = self._make_rest_call(action_result, 'tasks/{}'.format(task_id), method=requests.get)

        if (not ret_val):

            if ('not find' in action_result.get_message()):
                return action_result.set_status(phantom.APP_ERROR, "Task ID, {}, not found".format(task_id))

            return phantom.APP_ERROR

        action_result.add_data(resp_json)

        summary = {}
        summary['task_status'] = resp_json.get('results', [{}])[0].get('task_state_state', 'UNKNOWN_STATE')
        summary['risk_score'] = resp_json.get('results', [{}])[0].get('tasks_owner_risk_score', 'UNKNOWN_STATE')
        action_result.set_summary(summary)

        return action_result.set_status(phantom.APP_SUCCESS, "Report successfully retrieved")

    def handle_action(self, param):

        ret_val = None

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()

        self.debug_print("action_id", self.get_action_identifier())

        if (action_id == self.ACTION_ID_TEST_CONNECTIVITY):
            ret_val = self._test_connectivity(param)
        if (action_id == self.ACTION_ID_DETONATE_FILE):
            ret_val = self._detonate_file(param)
        if (action_id == self.ACTION_ID_GET_REPORT):
            ret_val = self._get_report(param)

        return ret_val


if __name__ == '__main__':

    import sys
    # import pudb
    # pudb.set_trace()

    if (len(sys.argv) < 2):
        print "No test json specified as input"
        exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = BCMASConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print (json.dumps(json.loads(ret_val), indent=4))

    exit(0)
