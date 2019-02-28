listA = ["Hi", "List",1,True]
print(listA)
listB = [1,2,3]
listB.append(4) #[1,2,3,4]
listB.insert(0,-1) #inserts element in the given index.
listB.insert(1,0)
listB.remove(4)
print(len(listB)) #5
#print(listB.index(6)) #ValueError: 6 is not in list
print(listA+listB) #adding listA and listB to get a new list with all elements
print("Hi" in listA) #checks if "Hi" is present in listA
print("World" in listB)
print("ello" in "Hello") #in can also be used for strings
print("world" not in "hello")
exit()
