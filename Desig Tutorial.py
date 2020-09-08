def isPrime(n):

    if n<=1:
        return False
    if n<=3:
        return False

    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while (i*i <= n):

        if n%i == 0 or n%(i+2) == 0:
            return False
        i = i+6
        print(i," ",i*i)


    return True

n = int(input("Enter Your Number: "))

if isPrime(n):
    print("Yes It is True")
else:
    print("It's Not Prime")