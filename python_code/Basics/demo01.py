myList1 = [1,2,3]
myList2 = myList1
myList3 = [1,2,3]
myList4 = myList3[:]

print("ID of myList1: ", id(myList1))
print("ID of myList2: ", id(myList2))
print("ID of myList3: ", id(myList3))
print("ID of myList4: ", id(myList4))
