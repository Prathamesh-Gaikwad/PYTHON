
iNo1 = int(input("\nEnter Number 1 : "))        #Enter Number 1 : 200
iNo2 = int(input("\nEnter Number 2 : "))        #Enter Number 2 : 100

print("\nBefore Swapping Number 1 is <{}> & Number 2 is <{}>".format(iNo1, iNo2))       #Before Swapping Number 1 is <200> & Number 2 is <100>

iNo1 = iNo1 + iNo2
iNo2 = iNo1 - iNo2
iNo1 = iNo1 - iNo2

print("\nAfter Swapping Number 1 is <{}> & Number 2 is <{}>".format(iNo1, iNo2))        #After Swapping Number 1 is <100> & Number 2 is <200>
