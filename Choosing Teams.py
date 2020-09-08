size,time = input().split()
ls = list(map(int,input().split()))
count = 0
for i in ls:
    if i+int(time)<=5:
        count +=1
print(int(count/3))

