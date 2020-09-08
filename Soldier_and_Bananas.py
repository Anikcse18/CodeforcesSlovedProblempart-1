ban_price,Dollar,pices = input().split()

tem =  0
for i in range(1,int(pices)+1):
    tem += (int(ban_price)*i)

x = tem - int(Dollar)
if x<=0:
    print(0)
else:
    print(x)
