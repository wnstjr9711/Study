#(a,b)행렬
#나선형으로1씩증가
#4X4예
#0 1 2 3
#1112134
#1015145
#9 8 7 6
#[[a[0]행],
# [a[1]행],
# [a[2]행]]
def ar(a,b):
    XY=[]
    for x in range(a):
    XY.append([])
    for i in range(a*b):
        for A in range(a):
            for B in range(b):
                XY[A].append(i)