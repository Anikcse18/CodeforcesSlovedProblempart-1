size = int(input())
cou = 0
ls1 = list(map(int,input().split(" ")))
ls2 = list(map(int,input().split(" ")))
ls3 = []

for i in range(1,len(ls1)):
    ls3.append(ls1[i])

for i in range(1, len(ls2)):
    ls3.append(ls2[i])

ls3 = sorted(ls3)
for i in range(len(ls3)-1):
    if ls3[i] == ls3[i+1]:

        cou +=1

if len(ls3)-cou == size:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

