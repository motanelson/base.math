print("\033c\033[40;37m\n")
import copy
def getlist(i:int): 
    l:list=[]
    for a in range(i):
        l.append(copy.copy(a))
    return l

def reverter(l:list):
    a:int=0
    ll:list=[]
    count=len(l)
    for aa in range(count):
        #print(count-1-aa)
        a=l[count-1-aa]
        ll.append(copy.copy(a))
    return ll


l=getlist(20)
print(l)
print(reverter(l))