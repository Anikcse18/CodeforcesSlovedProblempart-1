x = int(input())
ls = []
cou = 0
while True:
    inpt = input()
    ls= [int(i) for i in inpt.split(" ")]
    if len(ls) == x:
     break


for i in ls:
    if i == 1:
        cou +=1
if cou == 0:
    print("EASY")
else:
    print("HARD")




