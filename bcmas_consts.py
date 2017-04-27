# --
# File: bcmas_consts.py
#
# Copyright (c) Phantom Cyber Corporation, 2017
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber.
#
# --

BCMAS_ERR_FROM_SERVER = "Got an unknwon error"
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
