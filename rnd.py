print("\033c\033[40;37m\n")
import random
import copy


def rnds(i:int,nn:int):
    r=[]
    for n in range(i):
        rr=int(random.random()*nn)
        r.append(copy.copy(rr))
    return r

a=rnds(100,50)
print(a)

