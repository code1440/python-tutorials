import boto3


def create_instance():
    ec2_resource = boto3.resource('ec2')
    instances = ec2_resource.create_instances(ImageId='ami-6871a115',
                MinCount=1, MaxCount=3,InstanceType='t2.micro',
                SecurityGroupIds=['sep06'],KeyName='fullstack')
    for instance in instances:
        print instance
        i=[]
        i.append(instance.id)
    ec2_client = boto3.client('ec2')
    waiter=ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=i)
    print ("Instance is Running now!")

create_instance()


def delete_instance():
    ec2_client = boto3.client('ec2') 
    tinstances = ec2_client.terminate_instances(InstanceIds=i ,DryRun=False)

    