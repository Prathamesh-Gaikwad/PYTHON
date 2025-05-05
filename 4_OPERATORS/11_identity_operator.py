iNo1 = iNo2 = 10

iNo3 = 20

print("\niNo1 is iNo2 : ", iNo1 is iNo2)            #iNo1 is iNo2 :  True

print("\niNo1 is not iNo2 : ", iNo1 is not iNo2)    #iNo1 is not iNo2 :  False

print("\niNo1 is not iNo3 : ", iNo1 is not iNo3)    #iNo1 is not iNo3 :  True

print("\ntype(iNo1) is int : ", type(iNo1) is int)  #type(iNo1) is int :  True

List1 = [1, 2, 3, 4]
List2 = [1, 2, 3, 4]

print("\nList1 is List2 : ", List1 is List2)        #List1 is List2 :  False

Tuple1 = (1, 2, 3, 4)
Tuple2 = (1, 2, 3, 4)

print("\nTuple1 is Tuple2 : ", Tuple1 is Tuple2)    #Tuple1 is Tuple2 :  True

Dict1 = {1 : "One", 2 : "Two", 3 : "Three", 4 : "Four"}
Dict2 = {1 : "One", 2 : "Two", 3 : "Three", 4 : "Four"}

print("\nDict1 is Dict2 : ", Dict1 is Dict2)        #Dict1 is Dict2 :  False
