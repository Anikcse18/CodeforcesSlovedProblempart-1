inp = int(input())

for i in range(1,inp+1):
    if i%2 != 0 :
        x = "I hate {}"
        if i != inp:
            print(x.format("that"),end=" ")
        else:
            print(x.format("it"),end=" ")


    else:
        x = "I love {}"
        if i != inp:
            print(x.format("that"),end=" ")
        else:
            print(x.format("it"),end=" ")
