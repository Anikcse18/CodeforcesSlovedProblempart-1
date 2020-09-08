x = int(input())
ls = []
count = 0
for i in range(x):
    ls.append(input())

for m in ls:
    if m == "X++" or m == "++X":
        count +=1
    else:
        count -=1
print(count)
