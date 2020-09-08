input_size = int(input())
n = 0
ls = []
for i in range(0,input_size):
    number = int(input())
    tm = number

    if number <= 10 or number == 10000:
        print(1)
        print(number)
    else:
        cou = 0
        rem = 0
        num = 10

        while number>0:
            rem = number%10
            if rem != 0:
                cou += 1
            ls.append(rem)
            number = int(number/10)

        if len(ls) == 2 and ls[0] == 0:
            print(1)
            print(tm)
            ls.clear()

        else:
            print(cou)
            for i in range(0,len(ls)):
               if ls[i] == 0:
                 num = num * 10

               else:
                  if i == 0:
                    print(ls[i],end=" ")

                  else:
                     print(ls[i]*num,end=" ")
                     num = num * 10

            ls.clear()
            print()










