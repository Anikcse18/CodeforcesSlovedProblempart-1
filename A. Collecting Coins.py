size = int(input())
for i in range(size):
    ls = list(map(int,input().split()))
    coin = ls[-1]
    ls = ls[0:3]
    ls.sort()
    a = ls[2]-ls[0]
    b = ls[2]-ls[1]
    sb = coin-(a+b)

    if sb<0 or sb%3 !=0:
        print("NO")

    else:
        if sb%3==0 or sb==0:
            print("YES")
