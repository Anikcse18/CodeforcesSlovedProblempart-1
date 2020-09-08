

matrix = []
col = 0
row = 0

for i in range(3):
    a = []
    for j in range(3):
        inp = int(input())
        if  inp==1:
            row = i
            col = j
        a.append(inp)

    matrix.append(a)

print(abs(row-2)+abs(col-2))

