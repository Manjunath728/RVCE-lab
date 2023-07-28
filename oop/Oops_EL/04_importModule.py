from magicmethod import *

obj1=ope()
obj2=ope()

obj1.input()
obj2.input()

while True:
	print("-"*50)
	menu=int(input("\n1)power\n2)mod\n3)equal0)EXIT\n enter your menu :"))
	print("-"*50)
	if menu==1:
		obj1**obj2
	elif menu==2:
		obj1%obj2
	elif menu==3:
		obj1==obj2
	elif menu==0:
		print("sucessfully exited")
		break
	else:
		print("please enter valid menu")
