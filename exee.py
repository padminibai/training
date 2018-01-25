class school:
	
	def _init_(self,name,age,regno,marks):
		self.name=name
		self.age=age
		self.regno=regno
		self.marks=marks

	def ref(self):
		print('name:"{}" ','age:"{}"','reg.no:"{}"','marks:"{}"'.format(self.name,self.age,self.regno,self.marks))


class student(school):
	
	def _init_(self,name,age,regno,marks,add):
		school._init_(self,name,age,regno,marks)
		self.add=add

	def ref(self):
		school.ref(self)
		print('name:"{}" ','age:"{}"','regno:"{}"','marks:"{}"','add:"{}'.format(self.name,self.age,self.regno,self.marks,self.add))



class teacher(school):

	def _init_(self,name,age,add,workingexp):
		student._init_(self,name,age,add)
		self.workingexp=workingexp

	def ref(self):
		student.ref(self)
		print('name:"{}"','age:"{}"','add:"{}"','working exp:"{}"'.format(self.name,self.age,self.add,self.workingexp))

s=student('mani',23,234,50,'musiri')
t=teacher('sara',32,'trichy',5)
mem=[s,t]

for mem in mems:
	mem.ref()


	
