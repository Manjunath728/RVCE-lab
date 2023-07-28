import mysql.connector as ms


class employee_table:
    def __init__(self):
        self.db = ms.connect(user="manjunath", password="Fire_master728",
                             host="localhost", database="helloworld")
        self.cursor = self.db.cursor()
        self.createTable()

    def createTable(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS employees (empid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), designation VARCHAR(25));")
        self.db.commit()

    def insert(self, name, designation):
        self.cursor.execute(
            "INSERT INTO employees(name, designation) VALUES (%s, %s)", [name, designation])
        self.db.commit()
        print("Inserted successfully")

    def display(self, empid):
        self.cursor.execute(
            "SELECT * FROM employees WHERE empid = %s", [empid])
        for i in self.cursor.fetchall():
            print(i)

    def update(self, empid, designation):
        self.cursor.execute("UPDATE employees SET designation = %s WHERE empid = %s", [
                            designation, empid])
        self.db.commit()
        print("Updated successfully")

    def delete(self, empid):
        self.cursor.execute("DELETE FROM employees WHERE empid = %s", [empid])
        self.db.commit()
        print("Deleted successfully")

    def close(self):
        self.db.close()

    def all(self):
        self.cursor.execute("SELECT * FROM employees")
        for i in self.cursor.fetchall():
            print(i)


employee = employee_table()

while True:
    print("=" * 100)
    print("Welcome to the employee database")
    print("=" * 100)
    print("1) Add employee details\n2) Show employee details\n3) Update employee details\n4) Delete employee details\n5) Display all employee details\n6) Close employee database\n")
    print("=" * 100)
    choice = int(input("Choice: "))

    if choice == 6:
        employee.close()
        break
    elif choice == 1:
        name = input("Employee name: ")
        des = input("Employee designation: ")
        employee.insert(name, des)
    elif choice == 2:
        empid = input("Enter employee ID: ")
        employee.display(empid)
    elif choice == 3:
        empid = input("Enter employee ID to update: ")
        des = input("What is the new designation: ")
        employee.update(empid, des)
    elif choice == 4:
        empid = input("Enter the employee ID to delete: ")
        employee.delete(empid)
    elif choice == 5:
        employee.all()
