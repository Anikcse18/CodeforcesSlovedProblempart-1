def index_count(ls,leng):

    new = []

    for i in range(leng):
        x1 = 1
        x2 = 1
        x3 = 1
        for j in range(len(ls)):
           if ls[j] == 1 and x1 == 1:
               print(j+1,end=" ")
               x1 = 0
               ls[j] = 0


           elif ls[j] == 2 and x2 == 1:

               print(j+1,end=" ")
               x2  =  0
               ls[j] = 0

           elif ls[j]== 3 and x3  == 1:
              print(j+1,end=" ")
              x3 = 0
              ls[j] = 0
        print()

        
size= int(input())
one=0
two=0
three=0
ls = list(map(int,input().split()))
mx = ls
mx.sort()

if 1 in ls and 2 in ls and 3 in ls:
    for i in mx:

        if i == 1:
                one += 1
        elif i==2:
                two+=1
        else:
                three +=1

        vl = []

    if one == 1 or two == 2 and three == 3:
        index_count(ls, 1)
    else:
        if one<=two and one<=three:

           print(one)
           index_count(ls, one)

        elif two<=one and two<=three:
           print(two)
           index_count(ls, two)



        else:
           print(three)
           index_count(ls, three)



else:
    print(0)



