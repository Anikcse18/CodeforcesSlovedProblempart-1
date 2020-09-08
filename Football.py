number = input()
zero = 0
one = 0
for i in number:
    if int(i) == 0:
        if zero<7:
            zero += 1
            one = 0


    else:
        if one<7:
            one +=1
            zero = 0
    if one == 7 or zero == 7:
        break
if one == 7 or zero == 7:
    print("YES")
else:
    print("NO")