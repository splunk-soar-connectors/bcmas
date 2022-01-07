[comment]: # "Auto-generated SOAR connector documentation"
# Malware Analysis Service

Publisher: Phantom  
Connector Version: 1\.0\.19  
Product Vendor: Symantec  
Product Name: Malware Analysis Service  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 3\.0\.284  

Integrate with Malware Analysis Service \(MAS\) to execute actions like detonate file and get report

[comment]: # "File: readme.md"
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
**api\_key** |  optional  | password | API Key
**timeout** |  optional  | numeric | Detonate timeout in mins
**verify\_server\_cert** |  required  | boolean | Verify server certificate

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

<p>This action requires the input file to be present in the vault\.<br><br>The action will wait up to the timeout \(set in asset configuration\) for the detonation to complete\. If the detonation does not complete before the timeout, use <b>get report</b> to get the final result of the detonation\. Some things to note\:<ul><li>The <b>environment</b> parameter can have the values <i>IntelliVM</i>, <i>SandBox</i>, or <i>Mobile IntelliVM</i>\.</li><li>The <b>priority</b> parameter can have the values <i>high</i>, <i>medium</i>, or <i>low</i>\.</li><li>The <b>profile</b> parameter only applies if the <b>environment</b> parameter is set to <i>IntelliVM</i>\.</li><li>The <b>owner</b> parameter defaults to the asset's <b>username</b> parameter if it is set\. If the asset <b>username</b> parameter is not set, the <b>owner</b> is required</li></ul></p>

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**vault\_id** |  required  | Vault ID of the file to detonate | string |  `vault id` 
**environment** |  required  | Environment in which to detonate the file | string | 
**profile** |  optional  | If environment is set to IntelliVM, ID or short name of the profile in which to detonate the file | string | 
**priority** |  required  | Priority with which to run the task | string | 
**source** |  optional  | Source of the file to detonate \(defaults to www\) | string | 
**label** |  optional  | A label to give the file to detonate \(defaults to the vault ID of the file\) | string | 
**description** |  optional  | A Description to give the file to detonate | string | 
**owner** |  optional  | An owner to assign to the file to detonate \(defaults to asset username if it is configured\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data\.\*\.request | string | 
action\_result\.data\.\*\.results\.\*\.samples\_label | string | 
action\_result\.data\.\*\.results\.\*\.samples\_owner | string | 
action\_result\.data\.\*\.results\.\*\.samples\_source | string | 
action\_result\.data\.\*\.results\.\*\.samples\_description | string | 
action\_result\.data\.\*\.results\.\*\.samples\_exec\_arguments | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.resource\_magic\_magic | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_md5 | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_size | numeric | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_owner | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.resource\_magic\_magic\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_sha256 | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_magic\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_read\_only | numeric | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_date\_added | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_resource\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_resource\_name | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_resource\_present | numeric | 
action\_result\.data\.\*\.results\.\*\.samples\_sample\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.samples\_date\_added | string | 
action\_result\.data\.\*\.results\.\*\.samples\_sample\_type | string | 
action\_result\.data\.\*\.results\.\*\.samples\_basic\_sample\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.samples\_basic\_resource\_id | numeric | 
action\_result\.data\.\*\.exec\_time | numeric | 
action\_result\.data\.\*\.api\_version | numeric | 
action\_result\.data\.\*\.server\_time | string | 
action\_result\.data\.\*\.results\_count | numeric | 
action\_result\.data\.\*\.results\.\*\.task\_queue\.name | string | 
action\_result\.data\.\*\.results\.\*\.task\_queue\.messages | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_env\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_task\_id | numeric |  `mas task id` 
action\_result\.data\.\*\.results\.\*\.tasks\_state\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_sample\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.task\_state\_state | string | 
action\_result\.data\.\*\.results\.\*\.tasks\_task\_start | string | 
action\_result\.data\.\*\.results\.\*\.environments\_env\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.task\_state\_state\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_storage\_class | numeric | 
action\_result\.data\.\*\.results\.\*\.environments\_env\_type | string | 
action\_result\.data\.\*\.results\.\*\.environments\_local\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.environments\_host\_type | string | 
action\_result\.data\.\*\.results\.\*\.tasks\_owner\_risk\_score | numeric | 
action\_result\.data\.\*\.results\.\*\.environments\_host\_label | string | 
action\_result\.data\.\*\.results\.\*\.tasks\_global\_risk\_score | numeric | 
action\_result\.data\.\*\.results\.\*\.task\_properties\.\*\.task\_properties\_name | string | 
action\_result\.data\.\*\.results\.\*\.task\_properties\.\*\.task\_properties\_sval | string | 
action\_result\.data\.\*\.results\.\*\.task\_properties\.\*\.task\_properties\_nval | string | 
action\_result\.data\.\*\.results\.\*\.task\_properties\.\*\.task\_properties\_task\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_env\_start | string | 
action\_result\.data\.\*\.results\.\*\.tasks\_env\_runtime | numeric | 
action\_result\.data\.\*\.results\.\*\.vm\_profiles\_vmp\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_exec\_arguments | string | 
action\_result\.data\.\*\.results\.\*\.tasks\_env\_return\_code | numeric | 
action\_result\.data\.\*\.results\.\*\.vm\_profiles\_short\_name | string | 
action\_result\.data\.\*\.results\.\*\.environments\_current\_task | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
action\_result\.summary\.risk\_score | numeric | 
action\_result\.summary\.task\_status | string | 
action\_result\.parameter\.vault\_id | string |  `vault id` 
action\_result\.parameter\.environment | string | 
action\_result\.parameter\.description | string | 
action\_result\.parameter\.priority | string | 
action\_result\.parameter\.profile | string | 
action\_result\.parameter\.source | string | 
action\_result\.parameter\.owner | string | 
action\_result\.parameter\.label | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get report'
Retrieve the analysis results of a file detonation

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**task\_id** |  required  | Task ID of the report to get | numeric |  `mas task id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data\.\*\.request | string | 
action\_result\.data\.\*\.results\.\*\.samples\_label | string | 
action\_result\.data\.\*\.results\.\*\.samples\_owner | string | 
action\_result\.data\.\*\.results\.\*\.samples\_source | string | 
action\_result\.data\.\*\.results\.\*\.samples\_description | string | 
action\_result\.data\.\*\.results\.\*\.samples\_exec\_arguments | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.resource\_magic\_magic | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_md5 | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_size | numeric | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_owner | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.resource\_magic\_magic\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_sha256 | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_magic\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_read\_only | numeric | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_date\_added | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_resource\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_resource\_name | string | 
action\_result\.data\.\*\.results\.\*\.sample\_resources\.\*\.sample\_resources\_resource\_present | numeric | 
action\_result\.data\.\*\.results\.\*\.samples\_sample\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.samples\_date\_added | string | 
action\_result\.data\.\*\.results\.\*\.samples\_sample\_type | string | 
action\_result\.data\.\*\.results\.\*\.samples\_basic\_sample\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.samples\_basic\_resource\_id | numeric | 
action\_result\.data\.\*\.exec\_time | numeric | 
action\_result\.data\.\*\.api\_version | numeric | 
action\_result\.data\.\*\.server\_time | string | 
action\_result\.data\.\*\.results\_count | numeric | 
action\_result\.data\.\*\.results\.\*\.task\_queue\.name | string | 
action\_result\.data\.\*\.results\.\*\.task\_queue\.messages | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_env\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_task\_id | numeric |  `mas task id` 
action\_result\.data\.\*\.results\.\*\.tasks\_state\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_sample\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.task\_state\_state | string | 
action\_result\.data\.\*\.results\.\*\.tasks\_task\_start | string | 
action\_result\.data\.\*\.results\.\*\.environments\_env\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.task\_state\_state\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_storage\_class | numeric | 
action\_result\.data\.\*\.results\.\*\.environments\_env\_type | string | 
action\_result\.data\.\*\.results\.\*\.environments\_local\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.environments\_host\_type | string | 
action\_result\.data\.\*\.results\.\*\.tasks\_owner\_risk\_score | numeric | 
action\_result\.data\.\*\.results\.\*\.environments\_host\_label | string | 
action\_result\.data\.\*\.results\.\*\.tasks\_global\_risk\_score | numeric | 
action\_result\.data\.\*\.results\.\*\.task\_properties\.\*\.task\_properties\_name | string | 
action\_result\.data\.\*\.results\.\*\.task\_properties\.\*\.task\_properties\_sval | string | 
action\_result\.data\.\*\.results\.\*\.task\_properties\.\*\.task\_properties\_nval | string | 
action\_result\.data\.\*\.results\.\*\.task\_properties\.\*\.task\_properties\_task\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_env\_start | string | 
action\_result\.data\.\*\.results\.\*\.tasks\_env\_runtime | numeric | 
action\_result\.data\.\*\.results\.\*\.vm\_profiles\_vmp\_id | numeric | 
action\_result\.data\.\*\.results\.\*\.tasks\_exec\_arguments | string | 
action\_result\.data\.\*\.results\.\*\.tasks\_env\_return\_code | numeric | 
action\_result\.data\.\*\.results\.\*\.vm\_profiles\_short\_name | string | 
action\_result\.data\.\*\.results\.\*\.environments\_current\_task | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
action\_result\.summary\.risk\_score | numeric | 
action\_result\.summary\.task\_status | string | 
action\_result\.parameter\.task\_id | numeric |  `mas task id` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 