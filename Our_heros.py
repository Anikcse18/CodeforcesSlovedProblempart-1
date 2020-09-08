inpt = input()
new_str =[]
count = 0
for i in range(len(inpt)):
    check = inpt[i] in new_str

    if check == False:
       new_str.append(inpt[i])
       count +=1

if count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
