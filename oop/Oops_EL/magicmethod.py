class ope:
	def __init__(self):
		self.li=[]
	def input(self):
		self.li=list(map(int,input("enter list ").split()))
	def __pow__(self,other):
		templi=[]
		for i in range(0,len(self.li)):
			templi.append(self.li[i]**other.li[i])
		print("adtion of 2 list elements is",templi)
	def __mod__(self,other):
		templi=[]
		for i in range(0,len(self.li)):
			templi.append(self.li[i]%other.li[i])
		print("subtract of 2 list elements is",templi)
	def __eq__(self,other):
		templi=[]
		for i in range(0,len(self.li)):
			templi.append(self.li[i]==other.li[i])
		print("multiplication of 2 list elements is",templi)
	