value = input()
deflt = "HQ9"
cou = 0


for i in range(len(value)):
    if value[i] in deflt:
                cou +=1


if cou>0 :
    print("YES")
else:
    print("NO")