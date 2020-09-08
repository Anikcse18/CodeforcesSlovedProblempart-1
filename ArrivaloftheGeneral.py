inpt = int(input())
small_index = 0
big_index = 0
count = 0
tem= 0

while True:
    x = input()
    ls = [int(i) for i in x.split(" ")]
    if len(ls) == inpt:
        break
for_small= 101
for_big = 0

for i in  range(0,len(ls)):

    if ls[i] > for_big:
        for_big = ls[i]
        big_index = i

    if ls[i] <= for_small:
        for_small = ls[i]
        small_index = i


if big_index > small_index:
    small_index = small_index+1

print(big_index+(inpt-1)-small_index)
