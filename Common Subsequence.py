total_size = int(input())
for i in range(total_size):
    row,col = input().split(" ")
    ls1 = list(map(int,input().split()))
    ls2 = list(map(int,input().split()))
    ls1.sort()
    ls2.sort()

    cou = False
    vl = 0
    for i in range(len(ls1)):
        for j in range(len(ls2)):
            if ls1[i] == ls2[j]:
                vl =ls1[i]
                cou = True
                break

    if cou:
        print("YES")
        print(1, vl)
    else:
        print("NO")




