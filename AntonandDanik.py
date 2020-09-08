size = int(input())
A=0
D=0

x = input()
for i in range(size):
    if x[i] == 'A':
        A +=1
    else:
        D +=1
if A==D:
    print("Friendship")
elif A>D:
    print("Anton")
else:
    print("Danik")
