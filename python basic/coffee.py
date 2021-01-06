#coffee
coffee=5
while True:
    money=int(input("돈을 넣어주세요:"))
    if money==300:
        print("커피를 줍니다")
        coffee=coffee-1
    elif money>300:
        print("%d원을 돌려주고 커피를 줍니다"%(money-300))
        coffee=coffee-1
    else:
        print("돈을 돌려주고 커피를 안줍니다")
        print("커피가 %d개 남았습니다"%coffee)
    if not coffee:
        print("판매종료")
        break