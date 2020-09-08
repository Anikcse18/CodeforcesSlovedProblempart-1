ls = []


def selection_sort(ls):
    temp = 0
    for i in range(len(ls)):
        main_num = i

        for j in range(i+1,len(ls)):

            if ls[main_num] > ls[j]:
                main_num = j
                
        temp = ls[main_num];
        ls[main_num] = ls[i];
        ls[i] = temp;


while True:
    put = input()
    ls = [int(x) for x in put.split()]

    if len(ls) == 4:
        break

selection_sort(ls)
print(ls)

print(ls[3] - ls[0], end=" ")
print(ls[3] - ls[2], end=" ")
print(ls[3] - ls[1])




