size = int(input())
ls = list(map(int,input().split()))
ls.sort()
max = ls[-1]
sum = 0
for i in range(size):
    sum += max - ls[i]

print(sum)



    