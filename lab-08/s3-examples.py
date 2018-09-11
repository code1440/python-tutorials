import boto3

my_bucket_name = "bcrbucket"

s3 = boto3.resource('s3')
bucket = s3.Bucket(my_bucket_name)
for obj in bucket.objects.all():
   print obj.key,obj.last_modified


s3	=	boto3.client('s3')

#	Get	a	paginator	and	iterate	through	each	page  
paginator	= s3.get_paginator('list_objects')
for	page in	paginator.paginate(Bucket=my_bucket_name):
    for	obj	in	page['Contents']:
        print(obj['Key'])



s3	=	boto3.resource('s3')
obj	=	s3.Object(my_bucket_name,'ny-census.csv')  
print(obj.content_type)  
print(obj.last_modified)

