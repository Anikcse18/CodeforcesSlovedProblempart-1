size = int(input())
for i in range(size):
    mx = 1
    ls = list(map(int,input().split()))

    for i in ls:
        if mx<i:
            mx = i

    rem = mx%ls[0]

    if rem>=ls[1]:
        if rem == 0 and ls[1] == 0 and ls[0] > ls[2] :
            print(rem)

        else:
            subs = rem - ls[1]
            print(mx - subs)


    else:

       rem = ls[1]- rem
       print(mx - (ls[0]-rem))











