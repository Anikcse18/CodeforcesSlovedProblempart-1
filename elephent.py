dis = int(input())
ls = [1,2,3,4,5]
count = 0
if dis in ls:
    print(1)
else:

    while dis>5:
        dis =dis-5
        count +=1
    print(count+1);

