def selection_sort(n):

    for i in range(len(n)-1):
        min = i
        for j in range(i+1,len(n)):
            if n[j]<n[min]:
                min = j

        tem = n[min]
        n[min] = n[i]
        n[i] = tem



number_of_mug,volum = input().split()
number_of_mug = int(number_of_mug)

volum = int(volum)
ls = list(map(int,input().split()))
coun = False
su = 0

selection_sort(ls)

for i in range(number_of_mug-1):
    su += ls[i]

if su <= volum:
    print("YES")
else:
    print("NO")




