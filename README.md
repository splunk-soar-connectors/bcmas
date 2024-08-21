[comment]: # "Auto-generated SOAR connector documentation"
# Malware Analysis Service

Publisher: Phantom  
Connector Version: 1.0.21  
Product Vendor: Symantec  
Product Name: Malware Analysis Service  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 3.0.284  

Integrate with Malware Analysis Service (MAS) to execute actions like detonate file and get report

[comment]: # "File: README.md"
[comment]: # "Copyright (c) 2017 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
## Authentication

The Malware Analysis Service (MAS) App can authenticate in two ways. It can use an API key, which
can be obtained from the MAS command line, or it can use the username and password of a MAS user. If
it is using a username and password, it will request a temporary API key from the MAS instance using
the supplied credentials to use for the duration of the action. If the account has a
non-administrator role, such as "Analyst", then performing file detonations and getting reports will
work with the username and password but not with a permanent API key.  
  
When configuring a MAS asset, either the API key parameter or the username and password parameters
must be set for the asset to work correctly. If both are set, the API key will take precedence. This
will be checked during **test connectivity** . The username parameter is optional, but can be set
without the password parameter, as it can be used as the default to the **detonate file** action's
owner parameter.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Malware Analysis Service asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**url** |  required  | string | URL of Malware Analysis Service instance
**username** |  optional  | string | Malware Analysis Service Username
**password** |  optional  | password | Malware Analysis Service Password
**api_key** |  optional  | password | API Key
**timeout** |  optional  | numeric | Detonate timeout in mins
**verify_server_cert** |  required  | boolean | Verify server certificate

### Supported Actions  
[test connectivity](#action-test-connectivity) - Checks connectivity with the configured Malware Analysis Service instance using either the API key, or the user credentials  
[detonate file](#action-detonate-file) - Run the file in the Malware Analysis Service instance and, if possible, retrieve the analysis results  
[get report](#action-get-report) - Retrieve the analysis results of a file detonation  

## action: 'test connectivity'
Checks connectivity with the configured Malware Analysis Service instance using either the API key, or the user credentials

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'detonate file'
Run the file in the Malware Analysis Service instance and, if possible, retrieve the analysis results

Type: **investigate**  
Read only: **True**

<p>This action requires the input file to be present in the vault.<br><br>The action will wait up to the timeout (set in asset configuration) for the detonation to complete. If the detonation does not complete before the timeout, use <b>get report</b> to get the final result of the detonation. Some things to note:<ul><li>The <b>environment</b> parameter can have the values <i>IntelliVM</i>, <i>SandBox</i>, or <i>Mobile IntelliVM</i>.</li><li>The <b>priority</b> parameter can have the values <i>high</i>, <i>medium</i>, or <i>low</i>.</li><li>The <b>profile</b> parameter only applies if the <b>environment</b> parameter is set to <i>IntelliVM</i>.</li><li>The <b>owner</b> parameter defaults to the asset's <b>username</b> parameter if it is set. If the asset <b>username</b> parameter is not set, the <b>owner</b> is required</li></ul></p>

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**vault_id** |  required  | Vault ID of the file to detonate | string |  `vault id` 
**environment** |  required  | Environment in which to detonate the file | string | 
**profile** |  optional  | If environment is set to IntelliVM, ID or short name of the profile in which to detonate the file | string | 
**priority** |  required  | Priority with which to run the task | string | 
**source** |  optional  | Source of the file to detonate (defaults to www) | string | 
**label** |  optional  | A label to give the file to detonate (defaults to the vault ID of the file) | string | 
**description** |  optional  | A Description to give the file to detonate | string | 
**owner** |  optional  | An owner to assign to the file to detonate (defaults to asset username if it is configured) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data.\*.request | string |  |  
action_result.data.\*.results.\*.samples_label | string |  |  
action_result.data.\*.results.\*.samples_owner | string |  |  
action_result.data.\*.results.\*.samples_source | string |  |  
action_result.data.\*.results.\*.samples_description | string |  |  
action_result.data.\*.results.\*.samples_exec_arguments | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.resource_magic_magic | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_md5 | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_size | numeric |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_owner | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.resource_magic_magic_id | numeric |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_sha256 | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_magic_id | numeric |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_read_only | numeric |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_date_added | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_resource_id | numeric |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_resource_name | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_resource_present | numeric |  |  
action_result.data.\*.results.\*.samples_sample_id | numeric |  |  
action_result.data.\*.results.\*.samples_date_added | string |  |  
action_result.data.\*.results.\*.samples_sample_type | string |  |  
action_result.data.\*.results.\*.samples_basic_sample_id | numeric |  |  
action_result.data.\*.results.\*.samples_basic_resource_id | numeric |  |  
action_result.data.\*.exec_time | numeric |  |  
action_result.data.\*.api_version | numeric |  |  
action_result.data.\*.server_time | string |  |  
action_result.data.\*.results_count | numeric |  |  
action_result.data.\*.results.\*.task_queue.name | string |  |  
action_result.data.\*.results.\*.task_queue.messages | numeric |  |  
action_result.data.\*.results.\*.tasks_env_id | numeric |  |  
action_result.data.\*.results.\*.tasks_task_id | numeric |  `mas task id`  |  
action_result.data.\*.results.\*.tasks_state_id | numeric |  |  
action_result.data.\*.results.\*.tasks_sample_id | numeric |  |  
action_result.data.\*.results.\*.task_state_state | string |  |  
action_result.data.\*.results.\*.tasks_task_start | string |  |  
action_result.data.\*.results.\*.environments_env_id | numeric |  |  
action_result.data.\*.results.\*.task_state_state_id | numeric |  |  
action_result.data.\*.results.\*.tasks_storage_class | numeric |  |  
action_result.data.\*.results.\*.environments_env_type | string |  |  
action_result.data.\*.results.\*.environments_local_id | numeric |  |  
action_result.data.\*.results.\*.environments_host_type | string |  |  
action_result.data.\*.results.\*.tasks_owner_risk_score | numeric |  |  
action_result.data.\*.results.\*.environments_host_label | string |  |  
action_result.data.\*.results.\*.tasks_global_risk_score | numeric |  |  
action_result.data.\*.results.\*.task_properties.\*.task_properties_name | string |  |  
action_result.data.\*.results.\*.task_properties.\*.task_properties_sval | string |  |  
action_result.data.\*.results.\*.task_properties.\*.task_properties_nval | string |  |  
action_result.data.\*.results.\*.task_properties.\*.task_properties_task_id | numeric |  |  
action_result.data.\*.results.\*.tasks_env_start | string |  |  
action_result.data.\*.results.\*.tasks_env_runtime | numeric |  |  
action_result.data.\*.results.\*.vm_profiles_vmp_id | numeric |  |  
action_result.data.\*.results.\*.tasks_exec_arguments | string |  |  
action_result.data.\*.results.\*.tasks_env_return_code | numeric |  |  
action_result.data.\*.results.\*.vm_profiles_short_name | string |  |  
action_result.data.\*.results.\*.environments_current_task | numeric |  |  
action_result.status | string |  |  
action_result.message | string |  |  
action_result.summary | string |  |  
action_result.summary.risk_score | numeric |  |  
action_result.summary.task_status | string |  |  
action_result.parameter.vault_id | string |  `vault id`  |  
action_result.parameter.environment | string |  |  
action_result.parameter.description | string |  |  
action_result.parameter.priority | string |  |  
action_result.parameter.profile | string |  |  
action_result.parameter.source | string |  |  
action_result.parameter.owner | string |  |  
action_result.parameter.label | string |  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |    

## action: 'get report'
Retrieve the analysis results of a file detonation

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**task_id** |  required  | Task ID of the report to get | numeric |  `mas task id` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.data.\*.request | string |  |  
action_result.data.\*.results.\*.samples_label | string |  |  
action_result.data.\*.results.\*.samples_owner | string |  |  
action_result.data.\*.results.\*.samples_source | string |  |  
action_result.data.\*.results.\*.samples_description | string |  |  
action_result.data.\*.results.\*.samples_exec_arguments | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.resource_magic_magic | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_md5 | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_size | numeric |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_owner | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.resource_magic_magic_id | numeric |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_sha256 | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_magic_id | numeric |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_read_only | numeric |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_date_added | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_resource_id | numeric |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_resource_name | string |  |  
action_result.data.\*.results.\*.sample_resources.\*.sample_resources_resource_present | numeric |  |  
action_result.data.\*.results.\*.samples_sample_id | numeric |  |  
action_result.data.\*.results.\*.samples_date_added | string |  |  
action_result.data.\*.results.\*.samples_sample_type | string |  |  
action_result.data.\*.results.\*.samples_basic_sample_id | numeric |  |  
action_result.data.\*.results.\*.samples_basic_resource_id | numeric |  |  
action_result.data.\*.exec_time | numeric |  |  
action_result.data.\*.api_version | numeric |  |  
action_result.data.\*.server_time | string |  |  
action_result.data.\*.results_count | numeric |  |  
action_result.data.\*.results.\*.task_queue.name | string |  |  
action_result.data.\*.results.\*.task_queue.messages | numeric |  |  
action_result.data.\*.results.\*.tasks_env_id | numeric |  |  
action_result.data.\*.results.\*.tasks_task_id | numeric |  `mas task id`  |  
action_result.data.\*.results.\*.tasks_state_id | numeric |  |  
action_result.data.\*.results.\*.tasks_sample_id | numeric |  |  
action_result.data.\*.results.\*.task_state_state | string |  |  
action_result.data.\*.results.\*.tasks_task_start | string |  |  
action_result.data.\*.results.\*.environments_env_id | numeric |  |  
action_result.data.\*.results.\*.task_state_state_id | numeric |  |  
action_result.data.\*.results.\*.tasks_storage_class | numeric |  |  
action_result.data.\*.results.\*.environments_env_type | string |  |  
action_result.data.\*.results.\*.environments_local_id | numeric |  |  
action_result.data.\*.results.\*.environments_host_type | string |  |  
action_result.data.\*.results.\*.tasks_owner_risk_score | numeric |  |  
action_result.data.\*.results.\*.environments_host_label | string |  |  
action_result.data.\*.results.\*.tasks_global_risk_score | numeric |  |  
action_result.data.\*.results.\*.task_properties.\*.task_properties_name | string |  |  
action_result.data.\*.results.\*.task_properties.\*.task_properties_sval | string |  |  
action_result.data.\*.results.\*.task_properties.\*.task_properties_nval | string |  |  
action_result.data.\*.results.\*.task_properties.\*.task_properties_task_id | numeric |  |  
action_result.data.\*.results.\*.tasks_env_start | string |  |  
action_result.data.\*.results.\*.tasks_env_runtime | numeric |  |  
action_result.data.\*.results.\*.vm_profiles_vmp_id | numeric |  |  
action_result.data.\*.results.\*.tasks_exec_arguments | string |  |  
action_result.data.\*.results.\*.tasks_env_return_code | numeric |  |  
action_result.data.\*.results.\*.vm_profiles_short_name | string |  |  
action_result.data.\*.results.\*.environments_current_task | numeric |  |  
action_result.status | string |  |  
action_result.message | string |  |  
action_result.summary | string |  |  
action_result.summary.risk_score | numeric |  |  
action_result.summary.task_status | string |  |  
action_result.parameter.task_id | numeric |  `mas task id`  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |  