size = int(input())
x = 0
ls1 = []
ls2= []

for i in range(size):
    x = int(input())
    div = int(x/2)
    sum_even = int(div*(div+1))
    odd_number = (div-1)*(div - 1)
    sum_odd =  0
    if (sum_even - odd_number )%2 == 0:
        print("NO")
    else:
        print("YES")
        for i in range(2,x+1,2):
            ls1.append(i)

        for i in range(1,x-1,2):
            sum_odd +=i
            ls2.append(i)
        ls2.append(sum_even - sum_odd)
        ls1 += ls2
        for i in range(len(ls1)):
            print(ls1[i],end=" ")
        print()
        ls1.clear()
        ls2.clear()


