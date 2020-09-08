def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

size = int(input())

for i in range(size):
    fr,sc = input().split(" ")
    fr = int(fr)
    sc = int(sc)
    vl = compute_lcm(fr,sc)
    if abs(fr-sc) <= 1:
        print(-1,-1)

    elif (sc*fr == vl):
        print(sc+1,fr-1)

    else:
        xf = fr
        xc = sc
        cou = 0
        while fr<sc:
            xf = xf+1
            xc = xc-1

            if compute_lcm(fr,sc)<=vl:
                print(fr,sc)
                break
            else:
                cou +=1
        if cou >0:
            print(xf,xc)










