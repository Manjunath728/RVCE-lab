while(1):
	print("1)String Operation\n2)Tuple operation\n 0)Exit")
	mainmenu=int(input("enter your choice"))
	if(mainmenu==1):
		print("String operation\n")
		string1=input("enter a string")
		while(1):
			print("1)String split\n2)check string conatin digit only\n3)check string conatin alphabet  only\n4)String title\n5)String strip")
			stringmenu=int(input("enter your choice"))
			if(stringmenu==1):
				print("the split of string is :",string1.split())
			elif(stringmenu==2):
				print("the given string is digit :",string1.isdigit())
			elif(stringmenu==3):
				print("the given string is aplhabet :",string1.isalpha())
			elif(stringmenu==4):
				print("the title of string is : ",string1.title())
			elif(stringmenu==5):
				print("stripping string is :",string1.strip())
			elif(stringmenu==0):
				break
			else:
				print("enter correct choice")


	elif(mainmenu==2):
		print("Tuple operation")
		tuple1=tuple(map(int,input("enter element").split()))
		while(1):
			print("1)sum\n2)sort\n3)min\n4)max\n5)index")
			tuplemenu=int(input("enter your choice : "))
			if(tuplemenu==1):
				print("the sum of tuple is ",sum(tuple1))
			elif(tuplemenu==2):
				print("the sorted  tuple is : ",sorted(tuple1))
			elif(tuplemenu==3):
				print("min element in tuple " ,min(tuple1))
			elif(tuplemenu==4):
				print("min element in tuple " ,max(tuple1))
			elif(tuplemenu==5):
				i=int(input("enter the element  for accesing index"))
				print(f"index of  {i} is {tuple1.index(i)}")
				break
			else:
				print(" enter correct choice")
	elif(mainmenu==0):
		break
	else:
		print("enter correct number")
