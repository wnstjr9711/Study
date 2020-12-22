from collections import defaultdict
def dig(n):
    a=[]
    dic={}
    dic=defaultdict(int)
    for x in range(1,n+1):
        X=list(str(x))
        a.extend(X)
    for Q in a:
        dic[Q]+=1
    return dic