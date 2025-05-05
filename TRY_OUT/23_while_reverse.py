#Reverse Of Number
No = int(input("\nEnter Number : "))        #Enter Number : 567

Temp = 0
while(No != 0):
    Temp = (Temp * 10) + (No % 10)
    '''
        ABOVE(6) : sum of digits sathi... Temp = Temp + (No % 10) change hoel 
    '''
    No = No // 10

print("\nReverse : ", Temp)                 #Reverse :  765
