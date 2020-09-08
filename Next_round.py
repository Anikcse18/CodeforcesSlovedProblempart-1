size_arry, stndr_number = input().split()
ls = []
count = 0
while True:
    x = input()
    ls = [int(x) for x in x.split(" ")]
    if len(ls) == int(size_arry):
        break

tem_number = ls[int(stndr_number)-1]



for x in ls:
   if x>=tem_number and x != 0:
       count +=1

print(count)
