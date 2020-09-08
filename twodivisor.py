import  math
def is_prime(x):

    count = 0
    for i in range(2,int((x/2)+1)):
        if x % i==0:
          count +=1

    if count==0:
        return True
    else:
        return False

def dev_cal(y):
    global div
    div = []
    for i in range(2,int(y/2)+1):

        if y%i==0:
            div.append(i)


inpt = int(input())
ls = []

while True:
    x = input()
    ls = [int(i) for i in x.split(" ")]
    if len(ls) == inpt:
        break


fir_list = []
sec_lis = []

for i in ls:

   if is_prime(i):

       fir_list.append(-1)
       sec_lis.append(-1)


   else:

       dev_cal(i)
       if len(div) == 1:
           fir_list.append(-1)
           sec_lis.append(-1)
       else:
           for m in range(len(div)-1):
               gcd_value = math.gcd(div[m] + div[m + 1], i)

               if gcd_value == 1:

                   fir_list.append(div[m])
                   sec_lis.append(div[m+1])
                   div.clear()
                   break


               else:
                   fir_list.append(-1)
                   sec_lis.append(-1)


for i in range(len(fir_list)):
    print(fir_list[i],end=" ")

print()

for i in range(len(sec_lis)):
    print(sec_lis[i],end=" ")







