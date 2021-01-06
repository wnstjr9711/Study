def d(n):
    sum=0
    ge=list(str(n))
    while ge:
        sum+=int(ge.pop())
    sum+=n
    return sum
#n는 d(n)의 제너레이터
#제너레이터가 없으면 셀프넘버
selfnum=[]
for x in range(1,5000):
    if d(x) in range(1,5001):
        selfnum.append(d(x))
SELFNUMBER=sorted(list(set(range(1,5001))-set(selfnum)))
print(SELFNUMBER)
sum=0
for i in SELFNUMBER:
    sum+=i
print(sum)