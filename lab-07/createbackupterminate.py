import sys

import boto3
from botocore.exceptions import ClientError


def create_instance():
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.create_instances(ImageId='ami-6871a115',
                MinCount=1, MaxCount=3,InstanceType='t2.micro',
                SecurityGroupIds=['sep06'],KeyName='fullstack')
    instance_ids = []
    for instance in instances:
        instance_ids.append(instance.id)
    ec2_client = boto3.client('ec2')
    waiter=ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=instance_ids)
    print ("Instance is Running now!")

create_instance()

def prepare_volume_list():
    mylist = []
    ec2 = boto3.resource('ec2')
    for volume in ec2.volumes.all():
        print(volume.volume_id)
        mylist.append(volume.volume_id)
    return mylist


def create_snapshot():
    ec2_resource = boto3.resource('ec2')
    list = prepare_volume_list()
    for l in list: 
        ec2_resource.create_snapshot(VolumeId=l, Description="Taking backup")

create_snapshot()