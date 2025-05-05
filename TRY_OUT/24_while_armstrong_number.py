#Armstrong Number

No = int(input("\nEnter Number : "))            #Enter Number : 1634
List = []

Temp = No
while(No > 0):
    List.append(No % 10)
    No = No // 10

Power = len(List)

Counter = 0
Sum = 0
while(Counter < len(List)):
    Sum = Sum + ((List[Counter])**Power)
    Counter = Counter + 1


if(Temp == Sum):
    print("\nArmstrong Number : True")          #Armstrong Number : True
else:
    print("\nArmstrong Number : False")
