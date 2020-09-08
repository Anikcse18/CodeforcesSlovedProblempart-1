
prob_num,time = input().split(" ")
prob_num = int(prob_num)
time = int(time)
ls = []
t_time = 240 - time
for i in range(1,prob_num+1):
    ls.append(i*5)
count = 0
tem = 0
for i in range(len(ls)):
    tem +=ls[i]

    if tem<=t_time:
        count +=1

print(count)


