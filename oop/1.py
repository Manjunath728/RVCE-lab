class employee:
    apply_raise=0.1
    def __init__(self):
        self.name=input("enter the name")
        self.emp=input("enter emp code")
        self.salary=int(input("enter salary"))
    def Apply_raise(self):
        self.salary=self.salary*self.apply_raise
    def display(self):
        print(self.name,self.emp,self.salary)
class dev(employee):
    apply_raise=.2
    def Apply_raise(self):
        self.salary=self.salary*self.apply_raise+self.salary
class manager(employee):
    apply_raise=.3
    def Apply_raise(self):
        self.salary=self.salary*self.apply_raise

e=employee()
e.display()
e.Apply_raise()
e.display()
e1=dev()
e1.display()
e1.Apply_raise()
e1.display()
e3=manager()
e3.display()
e3.Apply_raise()
e3.display()
