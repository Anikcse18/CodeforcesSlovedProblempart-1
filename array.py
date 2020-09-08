x = input()
ls = [int(i) for i in x if i !='+']
count = 0
ls.sort()
for i in range(len(ls)):
    if i != (len(ls)-1):
        print(ls[i],end='')
        print("+",end='')
    else:
        print(ls[i])


