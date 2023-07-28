while True:
	print(" 1)set \n 2)list")
	menu=int(input("enter menu number"))
	if menu==1:
		set1=set(map(int,input("enter set 1").split()))
		set2=set(map(int,input("enter set 2").split()))
		while True:
			
			
			print("\n\n\n\n01)s1 is equalent to s2 \n02)s1 is not equalent to s2 \n03)s1 is proper subset to s2 \n04)the set element is presisly ne s1 or s2 \n05)s1 is super set of s2 " )
			listmenu=int(input("enter your menu "))
			if listmenu==1 :
				print(set1==set2)
			elif listmenu==2 :
				print(set1!=set2)
			elif listmenu==3 :
				print(set2<set2)
			elif listmenu==4 :
				print(set1^set2)
			elif listmenu==5 :
				print(set1>=set2)
			else :
				print("enter the valid menu")
	elif menu==2:
		li=list(map(int,input("enter list ").split()))
		while (1) :
			print("\n\n\n1)index 2)count 3)min 4)max 5)sum ")
			listmenu=int(input(""))
			if(listmenu==1):
				element=int(input("enter element to find its index "))
				
				print("index of ",element ," is " ,li.index(element))
			elif(listmenu==2):
				element=int(input("enter element to count in list "))
				
				print("count of ",element ," is " ,li.count(element))
			elif(listmenu==3):
				print("min element in list " ,min(li))
			elif(listmenu==4):
				print("max element in list " ,max(li))
			elif(listmenu==5):
				print("sum element in list " ,sum(li))
			elif(listmenu==0):
				print("succesfully exited from menu ")
				break
			else:
				print("invalid option or press 0 for exit")

