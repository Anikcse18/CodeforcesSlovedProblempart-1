x = int(input())
tem=0
ls = []
while True:
    s = input()
    ls = [int(i) for i in s.split(" ") ]
    if len(ls) == x:
       break
for i in ls:
    tem +=i


print("{:.12f}".format(round((tem/x),12)))