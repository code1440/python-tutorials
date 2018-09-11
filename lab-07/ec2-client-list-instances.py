import boto3

ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances()
#print(response)

for k,v in response.items():
    if k == 'Reservations':
        for instance in v:
            for i,vv in instance.items():
               if i == 'Instances':
                   for ii in vv:
                    print ii['PublicDnsName']
                
