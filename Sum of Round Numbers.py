size = int(input())
ls = []

for i in range(size):
    vlu = input()
    x = int(vlu)
    incre = 1
    lngth = len(vlu)

    while lngth !=-1:
        rem = int((x%10)*incre)
        x = int(x/10)

        if rem > 0:
            ls.append(rem)

        lngth -= 1
        incre *=10
    print(len(ls))
    for i in ls:
        print(i,end=" ")
    print()
    ls.clear()



