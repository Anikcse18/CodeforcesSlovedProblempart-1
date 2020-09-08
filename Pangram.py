ls = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
count = 0
size = int(input())
set1 = list(set(input().lower()))
if len(set1) >=26:
    for i in range(len(set1)):
        if set1[i] in ls:
            count +=1
    if count == 26:
        print("YES")
    else:
        print("NO")
else:
    print("NO")