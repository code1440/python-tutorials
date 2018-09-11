import boto3

ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances()
<<<<<<< HEAD
# print(response)

for k,v in response.items():
    if k == "Reservations":
        for instance in v:
            for i,vv in instance.items():
                if i == 'instances':
                    for ii in vv:
                        print ii ['PublicDnsName'] 



                       
=======
#print(response)

for k,v in response.items():
    if k == 'Reservations':
        for instance in v:
            for i,vv in instance.items():
               if i == 'Instances':
                   for ii in vv:
                    print ii['PublicDnsName']
                
>>>>>>> 93d8c61036afb01214a8bdbe4a788181b66a7dba
