
size_loop = int(input())
empty_list = []

for x in range(0,size_loop):
    empty_list.append(input())


for ch in empty_list:
    if len(ch)>10:

        print(ch[0],end="")
        print((len(ch)-2),end="")
        print(ch[len(ch) - 1])


    else:
        print(ch)



