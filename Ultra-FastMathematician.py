first = input()
second = input()
ls = []
for i in range(len(first)):
    if first[i]!=second[i]:
        ls.append(1)
    else:
        ls.append(0)

for i in  range(len(ls)):
    print(ls[i],end="")
