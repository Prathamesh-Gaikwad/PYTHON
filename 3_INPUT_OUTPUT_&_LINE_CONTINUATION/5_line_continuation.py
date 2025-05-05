#line continuation in python

#explicit line contniuation

iSum = 10 + \
       20 + \
       30

print("\niSum = ", iSum)        #iSum =  60

#implicit line continuation
Numbers = [10, 20, 30,
           40, 50, 60]

print("\nNumbers = ",
      Numbers)                  #Numbers =  [10, 20, 30, 40, 50, 60]

