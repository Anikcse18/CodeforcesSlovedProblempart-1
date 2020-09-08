
size = int(input())

if size%2==0:
    print(int(size/2))
    for i in range(int(size/2)):
        print(2,end=" ")
elif size == 5:
    print(2)
    print(2,3)
else:
    sum = size - 3
    print(int(sum/2)+1)
    for i in range(int(sum/2)):
        print(2,end=" ")
    print(3)




