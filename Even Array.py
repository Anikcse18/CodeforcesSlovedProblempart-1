size = int(input())
for i in range(size):
    l_size = input()
    even = 0
    odd = 0
    ls = list(map(int,input().split()))
    for i in range(len(ls)):
        if i%2==0:
            if ls[i]%2 == 0:
                pass
            else:
                even +=1
        elif i%2 !=0:
            if ls[i]%2 != 0:
                pass
            else:
                odd +=1
    if even == odd:
        print(even)
    elif even ==0 and odd == 0:
        print(even)
    else:
        print(-1)




