d=dict()

class emp:
    def input(self):
        self.name=input("enter employee details \nName: ")
        self.address=input("adress: ")
        self.pan=input("PAN: ")
        self.basic=int(input("Basic Salary: "))
        self.hra=self.basic*.2
        self.da=self.basic*.25
        self.deduct=self.basic*.1
        self.tds=self.basic*.15
        self.update()
    def update(self):
        d.update({self.name:{"name":self.name,"basic":self.basic}})
        print("added to database sucessfully")
    def search(self,name):
        flag=0
        for key in d:
            if key==name:
                print("!!!!!!!!! employee found !!!!!!! \n ")
                for key1 in d[key]:
                    print(key1," : ",d[key][key1])
                flag=1
                break
                
        if not flag:
            print("Employe deatils not found")
    def printEmp(self):
        for key in d:
            print(key," : \n")
            for key1 in d[key]:
                    print(key1," : ",d[key][key1])
employee=emp()
while True:
    choice=int(input("1)add\n2)search\n3)print"))
    if choice==1:
        employee.input()
    elif choice==2:
        employee.search(input("enter name"))
    elif choice==3:
        employee.printEmp()

            