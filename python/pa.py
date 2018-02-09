class Office:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print("display the detailes: {}".format(self.name))
	def tell(self):
		print('name: "{}" age: "{}" '.format(self.name,self.age))
class Emp(Office):
	def __init__(self ,name,age,salary):
		Office.__init__(self,name,age)
		self.salary = salary
		print('display the detailes: {}'.format(self.name))
	def tell(self):
		Office.tell(self)
		print('salary: "{:d}" '.format(self.salary))
class Mang(Office):
	def __init__(self ,name,age,credits):
		Office.__init__(self,name,age)
		self.credits= credits
		print('display the detailes: {}'.format(self.name))
	def tell(self):
		Office.tell(self)
		print('credits: "{:f}" '.format(self.credits))
e = Emp('RRB', 66, 60000)
m = Mang('sara', 40, 5.0)
members =[e,m]
for member in members:
	member.tell()

 


