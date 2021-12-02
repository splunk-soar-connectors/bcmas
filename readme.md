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
