#input & output in python

Name = input("\nEnter Your Name : ")        #Enter Your Nmae : Prathamesh Bapu Gaikwad

print("\nYou Entered : ", Name)             #You Entered :  Prathamesh Bapu Gaikwad

#formatting of output using 'format()' method

Age = input("\nEnter Your Age : ")          #Enter Your Age : 21

print("\nYou Entered : ", Age)              #You Entered :  21

print('\nMy Name is "{}" and My Age is "{}"'.format(Name, Age))             #My Name is "Prathamesh Bapu Gaikwad" and My Age is "21"

print("\nAge of this person is {1} whose Name is {0}".format(Name, Age))    #Age of this person is 21 whose Name is Prathamesh Bapu Gaikwad

'''
In format() method counting start form 0th index...
'format()' method which is visible to any string object
'''

#---------------------------------------------------------------------------------------------------------------------------------------------

iAge = int(input("\nEnter Age : "))                                 #Enter Age : 21

fPercentage = float(input("\nEnter Percentage : "))                 #Enter Percentage : 94.40

strName = input("\nEnter Name :")                                   #Enter Name :Prathamesh

print("\nYou Entered Name  & Age as '{}' as '{}' with your percentage as '{}' ".format(strName, iAge, fPercentage))    #You Entered Name  & Age as 'Prathamesh' as '21' with your percentage as '94.4'

print("\ntype(strName) : ", type(strName))              #type(strName) :  <class 'str'>

print("\ntype(fPercentage) : ", type(fPercentage))      #type(fPercentage) :  <class 'float'>

print("\ntype(iAge) : ", type(iAge))                    #type(iAge) :  <class 'int'>
