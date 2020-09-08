size = int(input())
list1 = []
list2 = []

for i in range(size):
    y = 1
    sum1 = 0
    sum2 = 0
    value = int(input())
    for i in range(value):
        if i<(int(value/2)):
            list1.append(2**y)
            y +=1
        else:
            list2.append(2 ** y)
            y += 1


    for i in range(len(list1)-1):

        sum1 += list1[i]
        sum2 += list2[i]

    sum1 = sum1+list2[-1]
    sum2 = sum2+list1[-1]

    list1.clear()
    list2.clear()
    print(abs(sum1-sum2))
