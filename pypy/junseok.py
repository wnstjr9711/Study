#총합
userinput=input("숫자를넣어주세요:")
total=0
numbers=userinput.split(',')
for x in numbers:
    total+=int(x)
print(total)