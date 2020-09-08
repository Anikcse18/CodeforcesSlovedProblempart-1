x = input()

low_case = 0
up_case = 0

for i in range(len(x)):
    if x[i].isupper():
        up_case +=1
    else:
        low_case +=1

if up_case>low_case:
    print(x.upper())
else:
    print(x.lower())
