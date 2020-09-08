size = int(input())

for i in range(size):
    fla = True
    a = input()
    ls = list(map(int,input().split()))


    for i in range(len(ls)):
        mx = ls[0]
        if mx == 0:
            pass
        else:
            for j in range(len(ls)):
                b = ls[j]
                if i != j and b !=0 :
                    if mx-b<=1 and mx !=0:
                        if mx>b:
                            ls[j] == 0
                        else:
                            ls[i] == 0
                    else:
                        fla = False
                        break

    if fla:
         print("YES")
    else:
         print("NO")