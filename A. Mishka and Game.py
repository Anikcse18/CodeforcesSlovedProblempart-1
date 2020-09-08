size = int(input())
Mishka = 0
Chris = 0
for i in range(size):
    a,b = input().split(" ")
    a = int(a)
    b = int(b)

    if a>b:
        Mishka +=1
    elif a<b:
        Chris +=1
    else:
        pass

if  Mishka>Chris:
    print('Mishka')
elif Mishka<Chris:
    print('Chris')
else:
    print('Friendship is magic!^^')