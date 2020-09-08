import math

text_case = int(input())

def is_prime()

for i in range(text_case):
    number = int(input())
    if number%2 == 0:
        print(number/2," ",number/2)
    else:
        def isPrime(n):

            # Corner case
            if n <= 1:
                return False

            # Check from 2 to n-1
            for i in range(2, n):
                if n % i == 0:
                    return False;

            return True

