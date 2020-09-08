
size = int(input())
def selection_sort(n):
    for i in range(len(ls) - 1):

        min_ind = i
        for j in range(i + 1, len(ls)):
            if ls[min_ind] > ls[j]:
                min_ind = j

        temp = ls[min_ind]
        ls[min_ind] = ls[i]
        ls[i] = temp



for i in range(size):
    ls = list(map(int,input().split()))

    if ls[0] == ls[1] or ls[0] == ls[2] or ls[1] == ls[2]:
        if ls[0]==ls[1]==ls[2]:
            print("YES")
            for i in range(3):
                print(ls[i],end=" ")
            print()


        else:
           selection_sort(ls)
           if ls[0]==ls[1] and ls[0]<ls[2]:
               print("NO")
           else:
               print("YES")
               print(ls[0],1,ls[2])

    else:
        print("NO")

