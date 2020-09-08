size = int(input())
count = 0
tem = 0
ls = list(map(int,input().split()))
for i in range(size):
   if tem == 0:
        if ls[i] == -1:
            count += 1
        else:
            tem = ls[i]
   else:
       tem +=  ls[i]

print(count)