size = int(input())
ls = []

for i in range(size):
    x = input()
    for i in range(0,len(x),2):
        ls.append(x[i])
    if len(x)%2== 0:
        ls.append(x[-1])
    for i in ls:
        print(i,end="")
    print()
    
    ls.clear()

