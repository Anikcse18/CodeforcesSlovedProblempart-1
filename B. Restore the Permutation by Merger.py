size = int(input())
tem = []
for i in range(size):
    x = int(input())
    ls = list(map(int,input().split()))
    for i in ls:
        if i in tem:
            pass
        else:
            tem.append(i)
    for i in range(x):
        print(tem[i],end=" ")
    print()
    tem.clear()




