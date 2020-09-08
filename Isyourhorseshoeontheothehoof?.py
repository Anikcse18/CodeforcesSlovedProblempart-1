ls = list(map(int,input().split(" ")))
cou = 0
for i in range(0,3):
    if ls[i] == ls[i+1]:
        cou +=1
print(cou)
