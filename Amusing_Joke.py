first = input()
second = input()
suffeld = input()
count = 0

first = first+second
if len(suffeld) != len(first):
    print("NO")
else:
    guest = sorted(first)
    mixe = sorted(suffeld)
    for i in range(len(first)):
        if guest[i] == mixe[i]:
            count +=1
    if count == len(first):
        print("YES")

    else:
        print("NO")

