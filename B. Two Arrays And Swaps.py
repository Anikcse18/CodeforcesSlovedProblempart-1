size = int(input())
for i in range(size):
    arr_size,swap = input().split(" ")
    arr_size = int(arr_size)
    swap = int(swap)
    temp = 0
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)

    suming = 0

    for i in range(swap):
        if a[i]<b[i]:
            temp = b[i]
            b[i] = a[i]
            a[i] = temp

    for i in range(len(a)):
        suming +=a[i]
    a.clear()
    b.clear()

    print(suming)
