size = int(input())
ls = []
con = 0
for i in range(size):
    ls.append(input())


for i in range(len(ls)):
    s = ls[i]

    if s[0] == 'O' and s[1] == 'O' and s[3] == 'O' and s[4] == 'O':

        ls[i] = '++|OO'
        con = 1
        break
    elif s[0] == 'O' and s[1] == 'O' and s[3] == 'O' and s[4] == 'X':

        ls[i] = '++|OX'
        con = 1
        break

    elif s[0] == 'O' and s[1] == 'O' and s[3] == 'X' and s[4] == 'O':

        ls[i] = '++|XO'
        con = 1
        break
    elif s[0] == 'O' and s[1] == 'O' and s[3] == 'X' and s[4] == 'X':

        ls[i] = '++|XX'
        con = 1
        break


    elif s[0] == 'X' and s[1] == 'O' and s[3] == 'O' and s[4] == 'O':
        ls[i] = 'XO|++'
        con = 1
        break

    elif s[0] == 'O' and s[1] == 'X' and s[3] == 'O' and s[4] == 'O':
        ls[i] = 'OX|++'
        con = 1
        break

    elif s[0] == 'X' and s[1] == 'X' and s[3] == 'O' and s[4] == 'O':
        ls[i] = 'XX|++'
        con = 1
        break

if con == 1:
    print("YES")
    for i in range(len(ls)):
        print(ls[i])
else:
    print("NO")