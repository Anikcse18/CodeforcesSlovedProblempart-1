import random
size = int(input())

for i in range(size):
    arr_size = int(input())
    randomlist = []

    for i in range(0,arr_size):
        n = random.randint(1,1000)
        randomlist.append(n)
    for i in range(0,arr_size):
        if randomlist[0] + randomlist[1] == randomlist[2]:
            print(randomlist[2]+1,end=" ")
        else:
            print(randomlist[i], end=" ")
    print()
