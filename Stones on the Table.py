size = input()
x = input()
j = 0
for i in range(len(x)-1):
    if x[i] == x[i+1]:
        j +=1


print(j)