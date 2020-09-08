
table = input()
ls = list(map(str,input().split()))
one = 0
two = 0
three = 0
for i in range(5):
    x = ls[i]

    if table[0] == x[0] and table[1] != x[1]:
        one +=1
    elif table[0]  != x[0] and table[1] == x[1]:
        two +=1
    elif table[0]  == x[0] and table[1] == x[1]:
        three +=1


if one > 0 or two > 0 or three > 0:
    print("YES")
else:
    print("NO")







