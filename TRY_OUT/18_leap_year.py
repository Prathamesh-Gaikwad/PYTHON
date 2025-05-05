year = int(input("\nEnter Year : "))

if(0 == (year % 4)):
    print("\n{} is Leap Year".format(year))
else:
    print("\nNot a Leap Year")
