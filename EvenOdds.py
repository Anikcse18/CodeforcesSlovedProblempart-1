reng,intrvl = input().split()
reng = int(reng)
intrvl = int(intrvl)
if reng%2==0:
    part = int(reng/2)

else:
    part = int(reng/2)+1



if intrvl<=part:
    output = (2 * intrvl) - 1


else:
    output = (intrvl - part)*2
print(output)