while True:
    b = int(input())
    b3 = b%2
    b2 = b//2%2
    b1 = b//4%2
    b0 = b//8
    d = 1000*b0+100*b1+10*b2+b3
    print(d)