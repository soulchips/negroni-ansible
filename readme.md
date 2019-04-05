# JMeter Cluster Automation


## Description
A set of ansible scripts that spin up EC2 instances and configure them to become a JMeter Cluster for distributed load and performance testing.

## Dependancies
- Ansible
- Python
- Boto3
- AWS CLI
    - install cli
    - add credentials to cli
    - add to path

## Gotchas
- check the python path in the 'group_vars/all' and ensure that the path is correct
- create 'keys' directory
- you will need to create a so ansible can access the test repo

## Commands
Spin up & configure EC2 instances

`ansible-playbook -i ./hosts jmeter-cluster.yml --extra-vars "@variables.json"`

Launch performance test

`ansible-playbook -i ./hosts smoke-test.yml --extra-vars "@variables.json"`

Terminate EC2 instances

`ansible-playbook -i ./hosts terminate_hosts.yml --extra-vars "@variables.json"`


ToDo:
autogenerate subnet if it doesnt exist
autocheck for user and update vars
tag/label instances for AWS console
repo keys in variables file
what if public repo - what if no key is needed