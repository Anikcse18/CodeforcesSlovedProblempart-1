size = int(input())
ls = []
ln = 0
cou = 0
for i in range(size):
    ls.append(int(input()))

for i in range(len(ls)-1):

    if ls[i] != ls[i+1]:
        cou +=1
        ln = ls[i]

if ln == ls[-1]:
    print(cou)
else:
    print(cou+1)






