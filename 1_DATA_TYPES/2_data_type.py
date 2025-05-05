#boolean
iNo1 = 2

iRet = iNo1 < 1

print("iNo1 < 1 : ", iRet)                          #iNo1 < 1 :  False

print(type(iRet))                                   #<class 'bool'>

#None
answer = None

if answer is None:
    print("\n",type(answer))                        #<class 'NoneType'>
    
#Numbers
iNo2 = 10

if iNo2 is 10:
    print("\niNo2 = ", iNo2)                        #iNo2 =  10

print(type(iNo2))                                   #<class 'int'>

#binary hexadecimal and octal
print("\n",0b00000010)                              # 2
print(type(0b00000010))                             #<class 'int'>

print("\n",0xFF)                                    # 255
print(type(0xFF))                                   #<class 'int'>

print("\n",0o7)                                     # 7
print(type(0o7))                                    #<class 'int'>

#float
fNo = 92.40
print("\nfNo = ", fNo)                              #fNo =  92.4
print(type(fNo))                                    #<class 'float'>

print(92e0)                                         #92.0
print(92e-1)                                        #9.2
print(92e1)                                         #920.0
print(type(92e0))                                   #<class 'float'>

#string
str1 = "He'll'o"
print("\nstr1 = ", str1)                            #str1 =  He'll'o

str1 = "Bye"
print("\nstr1 = ", str1)                            #str1 =  Bye
print(type(str1))                                   #<class 'str'>

#complex number
Num = 1+2j
print("\nNum = ", Num)                              #Num =  (1+2j)

print("\nNum.Real = ", Num.real)                    #Num.Real =  1.0
print ("\nNum.imaginary = ", Num.imag)              #Num.imaginary =  2.0

print(type(Num))                                    #<class 'complex'>

#list
price = [15, 16000]
Items = ["Toothbrush", "phone",price]   
print("\n",type(Items))                             #<class 'list'>
print(Items)                                        #['Toothbrush', 'phone', [15, 16000]]

Items[0] = "Toothpaste"
print("\n",Items)                                   #['Toothpaste', 'phone', [15, 16000]]

print("\n",Items + Items)                           #['Toothpaste', 'phone', [15, 16000], 'Toothpaste', 'phone', [15, 16000]]

print("\n",Items * 2)                               #['Toothpaste', 'phone', [15, 16000], 'Toothpaste', 'phone', [15, 16000]]

print("\n",Items)                                   #['Toothpaste', 'phone', [15, 16000]]

List = list(str1)
'''
    ABOVE(76):list() function conversion towards list sathi vaapartat..
'''
print("\n",List)                                    #['B', 'y', 'e']

print("\nList[0] : ", List[0])                      #List[0] :  B

#tuple
Write = ("Script", "letters", "Essays")
Read = ("Swarjya", "Marathi", "Hindi", Write, Items)

Items[1] = "motog62/5g"
#Write[3] = "dialog"                                #TypeError: 'tuple' object does not support item assignment
'''
    ABOVE(89):tuple change cha nahi pan...assignment cha karu shkat nahi..
'''
print("\n",type(Read))                              #<class 'tuple'>
print("\n",Read)                                    #('Swarjya', 'Marathi', 'Hindi', ('Script', 'letters', 'Essays'), ['Toothpaste', 'motog62/5g', [15, 16000]])
print("\n",Items)                                   #['Toothpaste', 'motog62/5g', [15, 16000]]
print("\n",Write[0])                                #Script  [tuples can be accessible but not assignable]

#dictionary
Date = (17,10,2002)

Password = {"abc/id" : 1234 , "sony/liv" : 12345, "BOD" : Date, None : Write}

print("\n",type(Password))                          #<class 'dict'>

print("\n",Password)                                #{'abc/id': 1234, 'sony/liv': 12345, 'BOD': (17, 10, 2002), None: ('Script', 'letters', 'Essays')}

print("\nPassword[abc/id] = ",Password["abc/id"])   #Password[abc/id] =  1234

Password[3] = {1 : Read}

print("\n",Password)                                #{'abc/id': 1234, 'sony/liv': 12345, 'BOD': (17, 10, 2002), None: ('Script', 'letters', 'Essays'), 3: {1: ('Swarjya', 'Marathi', 'Hindi', ('Script', 'letters', 'Essays'), ['Toothpaste', 'motog62/5g', [15, 16000]])}}

print("\n",Password.keys())                         #dict_keys(['abc/id', 'sony/liv', 'BOD', None, 3])

print("\n",Password.values())                       #dict_values([1234, 12345, (17, 10, 2002), ('Script', 'letters', 'Essays'), {1: ('Swarjya', 'Marathi', 'Hindi', ('Script', 'letters', 'Essays'), ['Toothpaste', 'motog62/5g', [15, 16000]])}])

print("\n",Password.copy())                         #{'abc/id': 1234, 'sony/liv': 12345, 'BOD': (17, 10, 2002), None: ('Script', 'letters', 'Essays'), 3: {1: ('Swarjya', 'Marathi', 'Hindi', ('Script', 'letters', 'Essays'), ['Toothpaste', 'motog62/5g', [15, 16000]])}}

Password1 = Password.copy()                         

print("\n",type(Password1))                         #<class 'dict'>

print("\nPassword1 = ", Password1)                  #Password1 =  {'abc/id': 1234, 'sony/liv': 12345, 'BOD': (17, 10, 2002), None: ('Script', 'letters', 'Essays'), 3: {1: ('Swarjya', 'Marathi', 'Hindi', ('Script', 'letters', 'Essays'), ['Toothpaste', 'motog62/5g', [15, 16000]])}}
