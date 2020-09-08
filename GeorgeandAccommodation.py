size = int(input())

cou = 0
for i in range(size):
    room,capacity = input().split()
    tem = int(capacity) - int(room)
    if tem>=2:
        cou +=1
print(cou)