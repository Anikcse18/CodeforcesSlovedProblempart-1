size = int(input())
matrix = []
for i in range(size):
    a = []
    for j in range(size):
        if i == 0 or j == 0:
            a.append(1)
        else:
            a.append(0)
    matrix.append(a)

for i in range(1,size):
    for j in range(1,size):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]


print(matrix[size-1][size-1])