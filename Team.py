prblm_set = int(input())
ls = []
sub = 0
tem = 0
for m in range(0,prblm_set):

    while True:
        x =input()
        ls = [int(m) for m in x.split(" ")]

        if len(ls) == 3:
            for r in ls:
                if r==1:
                    sub +=1
            if sub>=2:
                tem +=1
                sub = 0
            sub = 0
            break
print(tem)

