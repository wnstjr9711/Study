a='이의덕,이재명,권종수,이재수,박철호,강동희,이재수,김지석,최승만,이성만,박영희,박수호,전경식,송우환,김재식,이유정'
a=a.split(',')
from collections import defaultdict
def Fname(x):
    d = {}
    d = defaultdict(int)
    for F in x:
        if list(F)[0]=='김':
            d['김']+=1
        elif list(F)[0]=='박':
            d['박']+=1
        else:
            d['나머지']+=1
    print(d)

Fname(a)

print(a.count('이재수'))

for doub in a:
    if a.count(doub)!=1:
        a.remove(doub)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
