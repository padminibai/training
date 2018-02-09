#assign the element
persons ={'name':'ladha','age':22,'salary':30000.00}
#display the element
print("all the deatils:",persons)
#assign the element
persons1 ={'name':'raj','age':22,'salary':30000.00}
#clear the element
persons1.clear()
#display the element
print("clear Deatiles:",persons1)
#copy the element 
per=persons.copy()
#display the element
print("copy element:",per)
#assign the element
name ={'a','b','c','d',}
# assign the valus
values ='letter'
# using from keys
letter=dict.fromkeys(name,values)
print("name:",letter)
#assign the element 
persons2 ={'name':'raj','age':22}
#get the element
print("name:",persons2.get('name'))
print("age:",persons2.get('age'))
print("salary:",persons2.get('salary'))
print("salary:",persons2.get('salary',30000.00))
#to view the item
print(persons.items())
#to display the keys
print(persons2.keys())
#to remove the element 
result=persons.popitem()
print("persons:",persons)
print("return value:",result)
#to set the default value
salary=persons2.setdefault('salary')
print("values:",persons2)
print("salary:",salary)
#to pop the element
element=persons.pop('name')
print("pop the element:",element)
print("remaining list:",persons)
#to displays the value
print(persons2.values())
#to update the values
a={1:'one',2:'apple'}
b={2:'orange'}
print ("a:",a)
a.update(b)
print("a:",a)








