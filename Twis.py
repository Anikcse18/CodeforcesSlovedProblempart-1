def sele_sort(n):
    for i in range(len(n)):
        min_num = i
        for j in range(i+1,len(n)):
            if n[min_num]>n[j]:
                min_num = j
        temp =  n[i]
        n[i] = n[min_num]
        n[min_num] = temp



x = int(input())
ls = list(map(int,input().split()))
sum1 =  0
sum2 = 0
coun = 0
for i in ls:
    sum1 += i
sum1 = int(sum1/2)
sele_sort(ls)

for i in range(len(ls)-1,-1,-1):
    sum2 += ls[i]
    coun +=1
    if sum2>sum1:
        break
print(coun)

