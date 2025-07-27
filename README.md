Here are instructions to navigate this repository. The contents of this repository are -
 - Ansible playbooks/templates for creating aws resources. All such ansible playbooks are in the directory 'ansi'
 - CloudFormation templates for creating aws resources. All such cloudFormation templates are in the directory 'cfn'
 - helper scripts in python to tasks on aws. these are resource specific. All such scripts are in the directory 'helper' with each resource having a sub-directory under it. e.g. 'rds' sub-directory in 'helper' directory has python scripts that does operations related to aws rds.
 - Further each sub-directory under the directory 'helper' as a file called 'instructions.txt'. This file describes the contenat and usage of the sub-directory and scripts in it.
