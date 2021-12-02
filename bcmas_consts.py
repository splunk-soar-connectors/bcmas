# File: bcmas_consts.py
#
# Copyright (c) 2017 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
BCMAS_ERR_FROM_SERVER = "Got an unknown error"
BCMAS_ERR_SERVER_CONNECTION = "Could not connect to the configured URL"
BCMAS_ERR_NOT_IN_VAULT = "Could not find specified vault ID in the vault"

BCMAS_SLEEP_SECS = 10
BCMAS_MSG_MAX_POLLS_REACHED = "Reached max polling attempts. Please use the task ID from this result as a parameter to the 'get report' action to query the report status."

# in minutes
BCMAS_MAX_TIMEOUT_DEF = 10

BCMAS_ENV_DICT = {
        "IntelliVM": "ivm",
        "SandBox": "sbx",
        "Mobile IntelliVM": "drd"}

BCMAS_TASK_COMPLETE_LIST = ['CORE_COMPLETE', 'SBX_ERROR', 'CORE_ERROR', 'CORE_INSERT_ERROR', 'IVM_ERROR']
