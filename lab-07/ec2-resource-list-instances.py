import boto3


ec2_resource = boto3.resource('ec2')

instances = ec2_resource.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id,instance.public_dns_name)
    
   

# Mac installation tip: 
# sudo pip install --ignore-installed six boto3
# Assignment : Create 3 instances in ec2 using ansible playbooked from last week.
# One the instance are created.
# Use Python boto3 library to Parse the ouput of boto reponse and find 
# 1. instance ids, ip address, privateDns, Public DNS


