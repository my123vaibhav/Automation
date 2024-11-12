import requests
payload={
    "name": "abcdserf"
}
r=requests.patch('https://reqres.in/api/users/2',data=payload)
print(r.json())



import sys
sys.exit(0)
import requests
payload={
    "name": "morpheus",
    "job": "zion resident"
}
r=requests.put('https://reqres.in/api/users/2',data=payload)
print(r.json())



import sys
sys.exit(0)
import requests
import json
mydat=open('abc.json','r').read()
print(mydat)
resp=requests.post('https://reqres.in/api/users',data=mydat)
print(resp)






import sys
sys.exit(0)
import requests
payload={
    "name": "morpheus",
    "job": "leader"
}
resp=requests.post('https://reqres.in/api/users',data=payload)
print(resp)
print(resp.json())
assert resp.json()['job']=='leader'



import sys
sys.exit(0)
import requests
resp=requests.get('https://reqres.in/api/users?page=2')
c=resp.json()['data']
for i in c:
    print(i['email'])


import sys
sys.exit(0)
print(resp.json()) #key:value
print(resp.text)   #plane text
print(resp.content) #bytes formate
print(resp.headers)
print(resp.cookies)
print(resp.url)



import sys
sys.exit(0)
code=resp.status_code
assert code==200,'code is not match'




import sys
sys.exit(0)
print(type(resp))   #status code
print(dir(resp))