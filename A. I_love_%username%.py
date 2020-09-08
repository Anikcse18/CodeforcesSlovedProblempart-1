loop_size = int(input())
ls = []
cou = 0
while True:
    t = input()
    ls = [int(x) for x in t.split(" ")]
    if len(ls) == loop_size:
        break

min = 0
for i in range(len(ls)):
    if ls[i]>min:
        min = ls[i]
        cou +=1
print(cou)