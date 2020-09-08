import math
cou = 0

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False

    return True

x = int(input())
if is_prime(x):
    print(1)
else:

    for i in range(2,int(x/2)+1):

        if x%i == 0:
            cou +=1
    print(cou+1)


