person,height  = input().split()
ls = []
cou = 0
while True:
    x = input()
    ls = [int(i) for i in x.split(" ")]
    if len(ls) == int(person):
        break
for i in ls:
    if int(i)<=int(height):
        cou +=1
    else:
        cou +=2
print(cou)
