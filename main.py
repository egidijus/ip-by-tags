#!/usr/bin/env python

import boto3

boto_connection = boto3.session.Session(profile_name='default')
ec2 = boto_connection.resource('ec2')

instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']
}, {
    'Name': 'tag:Service',
    'Values': ['Elk']
}, {
    'Name': 'tag:Env',
    'Values': ['test']
}, {
    'Name': 'tag:Role',
    'Values': ['Elasticsearch']
}])


def ip_address(list):
    addresses = []
    for instance in instances:
        addresses.append(instance.private_ip_address)
    return addresses


addresses_for_ansible = print(*ip_address(list), sep=",")
