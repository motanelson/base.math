print("\033c\033[40;37m\n")
import copy
def getlist(i:int): 
    l:list=[]
    for a in range(i):
        l.append(copy.copy(int(a)))
    return l

def means(l:list):
    a:list=[]
    total=0
    count=0
    for aa in l:
        total=total+aa
        count=count+1
    total=total/count
    return total


l=getlist(20)
print(l)
print(means(l))