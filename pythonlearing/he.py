def func_sum( a_list ):
    a_sum=0
    for i in range(len(a_list)):
        if a_list[i]%2==0:
            a_sum+=a_list[i]
    return a_sum

import math
def dunc_v (r1,r2,h):
    s1=math.pi* r1**2
    s2=math.pi*r2**2
    v1=s1*h
    v2=s2*h
    v=v1-v2
    return v
