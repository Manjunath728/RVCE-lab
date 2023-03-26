class ope:
    def __init__(self) :
        self.li=[]
    def aceept(self):
        n=int(input("enter length of list"))
        for i in range(0,n):
            e=int(input ("enter element "))
            self.li.append(e)
        print("your list : ",self.li)
    def __add__(self,other):
        newlist=[]
        for i in range(0,len(self.li)):
            newlist.append(self.li[i]+other.li[i])
        print("your new list",newlist)




        
