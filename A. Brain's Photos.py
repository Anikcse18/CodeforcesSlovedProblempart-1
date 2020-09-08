row,col = input().split()
row = int(row)
col = int(col)
matrix = []
blckWhite = 0
color = 0
for i in range(row):
    a = []
    a = list(map(str,input().split()))

    matrix.append(a)

for i in range(row):
    for j in range(col):
        if matrix[i][j] == 'W' or matrix[i][j] == 'G' or matrix[i][j] == 'B':

          blckWhite +=1
        else:

          color +=1

if color>0:
    print("#Color")

else:
    print("#Black&White")