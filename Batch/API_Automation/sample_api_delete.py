'''
GET---url
POST----> url,payload
PUT----> url,payload
Patch----> url,payload
Delete----> json----> url
200
201
202
204

401
500--->

'''
import time
import requests
resp=requests.get('https://the-internet.herokuapp.com/basic_auth',auth=('admin','admin'))
print(resp.elapsed.total_seconds())
assert resp.elapsed.total_seconds()<1,'Test case is failed'


import sys
sys.exit(0)
r=requests.get('http://httpbin.org/delay/1',timeout=3)
after=time.time()
actualtime=after-before
assert actualtime<5,'This is failed'

import sys
sys.exit(0)
resp=requests.delete('https://reqres.in/api/users/2')
#print(resp.json())
#print(resp.status_code)
assert resp.status_code==200, 'User deletion not performed'