size = int(input())
for i in range(size):
    row,col = input().split(" ")
    row = int(row)
    col = int(col)
    if row%2 == 0 and col%2 == 0:
        print(int((row*col)/2))

    elif row%2 != 0 and col%2 != 0:
        rm = int(row/2)*col + int(col/2)+1
        print(rm)
    elif row%2 !=0 and col%2 == 0:
        rm = int(row / 2) * col + int(col / 2)
        print(rm)

    elif row%2 ==0 and col%2 != 0:
        rm = int(row / 2) * col
        print(rm)