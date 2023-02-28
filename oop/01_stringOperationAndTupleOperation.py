str1=input("enter a string :")
print("""1.Find string length\n 2.convert to Caps \n3.convert to lowercase\n4.to reverse a string\n5.to capitaize string\n 6.to replace char\n 7.to find letter \n9.to repeat n times \n 10.to swapCase\n""")
while(1):
	num=int(input("enter a your number :"))
	if(num==1):
		print("String length is :"+str(len(str1)))
	elif (num==2):
		print("the upperCase is :"+str1.upper())
	elif (num==3):
                print("the LoweCase is :"+str1.lower())
	elif (num==4):
                print("the reverse string is :"+str1[::-1])
	elif (num==5):
                print("the capitalize of string  is :"+str1.title())
	elif (num==6):
		rep=input("enter a charecter to replace a :")
		print("the replaced string  is :"+str1.replace('a',rep))
	elif (num==7):
		fi=input("enter a charecter to find")
		print("1 means present ,-1 means not present : :"+str(str1.find(fi)))
	elif (num==8):
		con=input("enter a string for concatination :")
		print("Ater concatination  "+str1+con)
	elif(num==9):
		re=int(input("enter how many time should it repeat" ))
		print(str1 * re)
	





