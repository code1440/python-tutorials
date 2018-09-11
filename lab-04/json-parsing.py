import json

with open("ec2.json") as f:
    content = f.read()

j = json.loads(content)
# print j['changed']
# print j['instance_ids']
#print j['instances'][0]
#print json.dumps(j,sort_keys=True,indent=4)

for k,v in j.items():
    if k == 'instances':
        for instance in v:
            for k,v in instance.items():
                if k == "dns_name":
                    print v

