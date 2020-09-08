cube = int(input())
m = 0
k = 1
sm = 0
if cube == 1:
    print(1)
else:
    while True:

      m +=k
      sm +=m
      if cube<=sm:
          break
      else:
        k +=1
    if cube == sm:
        print(k)
    else:

        print(k-1)



