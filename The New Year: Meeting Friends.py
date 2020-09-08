def selectio_sor(n):
    for i in range(len(n)-1):
        min = i

        for j in range(i+1,len(n)):
            if n[min]>n[j]:
                min = j

        tem = n[i]
        n[i] = n[min]
        n[min] = tem
ls = list(map(int,input().split()))
selectio_sor(ls)
print(ls[2] - ls[0])


