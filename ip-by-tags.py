#!/usr/bin/env python

import boto3
import argparse

# you can use this script like this:
# ansible -i "$(./ip-mmkay.py test web)," all -m shell -a "rpm"


parser = argparse.ArgumentParser()
parser.add_argument("AWS_PROFILE", default='default', nargs="?", help="which aws profile configured in ~/.aws/credentials should we use?")
parser.add_argument("INSTANCE_TAG_NAME", default='server', nargs='?', help="type in the Name tag of the aws ec2 instance")

args = parser.parse_args()

aws_boto3 = boto3.session.Session(profile_name=args.AWS_PROFILE)
ec2 = aws_boto3.client('ec2')

# # debugging credentials
# sts = boto3.client('sts')
# print(sts.get_caller_identity())

instances = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        },
        {
            'Name': 'tag:Name',
            'Values': [args.INSTANCE_TAG_NAME]
        }
    ]
    )

instances = instances['Reservations']

def ip_address(list):
    addresses = []
    for instance in instances:
        addresses.append(instance['Instances'][0]['PrivateIpAddress'])
    return addresses

addresses_for_ansible = print(*ip_address(list), sep = ",")

