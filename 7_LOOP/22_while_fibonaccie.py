#Fibonaccie Sequence

Temp1 = Temp2 = 0

No = int(input("\nEnter Number : "))

while(No > 0):
    if(0 == Temp1 and 0 == Temp2):
        print("\n",Temp1)
        No = No - 1
        if(No <= 0):
            break
        Temp2 = Temp2 + 1
        print("\n",Temp2)
        No = No - 1
    else:
        Temp2 = Temp1 + Temp2
        Temp1 = Temp2 - Temp1
        print("\n",Temp2)
        No = No - 1
'''
    o/p:
        Enter Number : 10
             0

             1

             1

             2

             3

             5

             8

             13

             21

             34
'''
