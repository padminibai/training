# defining the list
list =[1,2,3,4,"cat","dog",7,8]
print("list:",list)
# defining the list2
mylist=[5,6,9,"rat","flower"]
#list is added
list.append(mylist)
#append list
print("append list:",list)
list.extend(mylist)
#extend list
print("extend list:",list)
# to insert the new element
list.insert(3,"hai")
#insert list
print("insert list:",list)
#to remove the element
mylist.remove("flower")
#remove list 
print("remove list:",list)
#to finding the position
index=list.index("dog")
print("find the position:",index)
#count element n
count=list.count("n")
# print the count value
print("count:",count)
# pop the element
return_value = list.pop(5)
print("pop element:",return_value)
print("pop list:",list)
# reverse the element
list.reverse()
#reverse list
print("reverse list:",list)
#clear the element
list.clear()
#clear list
print("clear list:",list)

