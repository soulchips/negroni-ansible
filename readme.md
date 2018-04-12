# JMeter Cluster Automation


## Description
A set of ansible scripts that spin up EC2 instances and configure them to become a JMeter Cluster for distributed load and performance testing.

## Dependancies
- Ansible
- AWS

## Commands
Spin up & configure EC2 instances

`ansible-playbook -i ./hosts jmeter-cluster.yml --extra-vars "@variables.json"`

Launch performance test

`ansible-playbook -i ./hosts smoke-test.yml --extra-vars "@variables.json"`

Terminate EC2 instances

`ansible-playbook -i ./hosts terminate_hosts.yml --extra-vars "@variables.json"`