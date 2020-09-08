ls = list(map(int,input().split(" ")))
st = input()
sm = 0
for i in st:

    sm += ls[int(i)-1]

print(sm)
