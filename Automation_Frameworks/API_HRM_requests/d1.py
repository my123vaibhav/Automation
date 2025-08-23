
import time

def get_curent_date():
    l1=time.ctime()
    l2=l1.split()
    if l2[1]=='Oct':
        l2[1]='10'
    s=l2[-1]+'-'+l2[1]+'-'+l2[2]
    return s
print(get_curent_date())
# print(l2[2]+'-'+l2[-1])