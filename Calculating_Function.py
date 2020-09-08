inpt = int(input())
ans = 0
if inpt%2==0:
    ans = int(inpt/2)
else:
    ans = int(-(inpt+1)/2)
print(ans)
