inpt = int(input())
typ = ["Tetrahedron","Cube","Octahedron","Dodecahedron","Icosahedron"]
val = [4,6,8,12,20]


ls = []
for i in range(inpt):
    ls.append(input())
temp = 0

for i in range(len(ls)):
    indx = typ.index(ls[i])
    temp += val[indx]
print(temp)



