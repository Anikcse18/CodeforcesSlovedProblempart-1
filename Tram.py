size = int(input())
remain = 0
x_e = 0
i_y = 0
comp = 0

for i in range(size):

   ex_it,intrnc = input().split()

   remain = (i_y - int(ex_it)) + int(intrnc)


   if i != 0:
    intrnc = remain

   if remain>comp:
       comp = remain


   i_y = int(intrnc)
   x_e = int(ex_it)
print(comp)
