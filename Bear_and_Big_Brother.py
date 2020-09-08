limak,bob = input().split()
count = 0
while True:

    if int(limak)> int(bob):
     break
    limak=int(limak)*3
    bob = int(bob)*2
    count +=1
print(count)
