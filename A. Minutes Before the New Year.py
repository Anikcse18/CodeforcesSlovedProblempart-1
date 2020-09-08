size = int(input())
st = 1440
for i in range(size):
    hr,mint = input().split(" ")
    hr = int(hr)
    mint = int(mint)
    tot = hr*60 + mint
    print(st-tot)

