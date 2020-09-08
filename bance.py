loop_size = int(input())
coun = 0

for i in range(loop_size):
    size,dis = input().split()
    x = str(input())

    if int(size) == len(x):
        if x[0] == "0":
            coun +=1
        for i in range(int(dis)+1,len(x),int(dis)+1):
          if x[i] == "0":
           coun += 1
    print(coun)
    coun = 0
