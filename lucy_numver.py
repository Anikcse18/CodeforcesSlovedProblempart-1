inpt = input()
cou = 0
for i in range(len(inpt)):
    if inpt[i] == '4' or inpt[i] == '7':
        cou +=1

if cou == 4 or cou == 7:
    print("YES")
else:
    print("NO")