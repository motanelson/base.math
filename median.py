print("\033c\033[40;37m\n")
import copy
def getlist(i:int): 
    l:list=[]
    for a in range(i):
        l.append(copy.copy(int(a)))
    return l
def mins(l:list):
    a:int=0
    count=0
    for aa in l:
        if count==0:
            a=aa
        else:
            if aa<a:
                a=aa
        count=count+1
    return a
def maxs(l:list):
    a:int=0
    count=0
    for aa in l:
        if count==0:
            a=aa
        else:
            if aa>a:
                a=aa
        count=count+1
        
    return a

def medians(l:list):
    a:list=[]
    total=0
    count=0
    mx=maxs(l)
    mn=mins(l)
    total=(mx-mn)/2 + mn
    return total


l=getlist(20)
print(l)
print(medians(l))