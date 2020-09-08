first ,second = input().split()
first = int(first)
second = int(second)

x = abs(first-second)
if x%2 == 0:
    if first>second:
        print(second,int(x/2))
    else:
        print(first, int(x / 2))


else:
    if first > second:
        print(second, int(x / 2))
    else:
        print(first, int(x / 2))

