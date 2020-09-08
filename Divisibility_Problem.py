size = int(input())
remainder = 0
for i in range(size):
    first ,second = input().split()
    first = int(first)
    second = int(second)

    if first<second:
        print(second-first)
    elif first%second == 0:
        print(0)
    else:
        remainder = first%second
        print(second-remainder)



