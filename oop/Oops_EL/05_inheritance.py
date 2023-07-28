class person:
	def input(self):
		self.name=input("name:")
		self.age=int(input("age:"))
		self.gender=input("gender:")

class employee(person):
	def input(self):
		super().input()
		self.company=input("company:")
		self.designation=input("designation:")

emp=employee()
emp.input()
for key in emp.__dict__:
	print("{} = {}".format(key,emp.__dict__[key]))
	

class sslc:
	def ss(self):
		self.sslc_marks=int(input("enter sslc marks:"))
		self.sslc_percentage=(self.sslc_marks/625)*100

class puc:
	def pu(self):
		self.puc_marks=int(input("enter puc marks:"))
		self.puc_percentage=(self.puc_marks/600)*100
		
class student(sslc,puc):
	def st(self):
		self.name=input("enter name:")
		self.age=int(input("enter age:"))
		super().ss()
		super().pu()

stu=student()
stu.st()
for key in stu.__dict__:
	print("{} = {}".format(key,stu.__dict__[key]))
		