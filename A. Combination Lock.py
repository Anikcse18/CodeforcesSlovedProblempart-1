size = int(input())
sta_num = str(input())
cal_number = str(input())
cou = 0

for i in range(len(sta_num)):
    s = int(sta_num[i])
    c = int(cal_number[i])
    if s==c:
        pass
    elif s>c:

        tem = 10+c
        n_tm = s-c

        if tem-s < n_tm:
            cou += tem-s


        else:
            cou +=n_tm

    elif s<c:
        tem = s+10
        n_tm = c-s

        if tem - c < n_tm:
            cou += tem-c

        else:
            cou += n_tm
print(cou)
