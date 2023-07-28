import mysql.connector as ms
from prettytable import PrettyTable

class EmployeeTable:
    def __init__(self):
        self.db = ms.connect(user="manjunath", password="Fire_master728", host="localhost", database="helloworld")
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS employees (empid INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), designation VARCHAR(25));")
        self.db.commit()

    def insert(self, name, designation):
        self.cursor.execute("INSERT INTO employees(name, designation) VALUES (%s, %s)", (name, designation))
        self.db.commit()
        print("Employee details inserted successfully")

    def display(self, empid):
        self.cursor.execute("SELECT * FROM employees WHERE empid = %s", (empid,))
        records = self.cursor.fetchall()

        if len(records) == 0:
            print("No employee found with the given ID.")
        else:
            table = PrettyTable()
            table.field_names = ["Emp ID", "Name", "Designation"]
            table.add_rows(records)
            print(table)

    def update(self, empid, designation):
        self.cursor.execute("UPDATE employees SET designation = %s WHERE empid = %s", (designation, empid))
        self.db.commit()
        print("Employee details updated successfully")

    def delete(self, empid):
        self.cursor.execute("DELETE FROM employees WHERE empid = %s", (empid,))
        self.db.commit()
        print("Employee details deleted successfully")

    def close(self):
        self.db.close()

employee = EmployeeTable()

while True:
    print("=" * 100)
    print("Welcome to the Employee Database")
    print("=" * 100)
    print("1) Add Employee Details")
    print("2) Show Employee Details")
    print("3) Update Employee Details")
    print("4) Delete Employee Details")
    print("5) Close Employee Database")
    print("=" * 100)

    choice = input("Choice: ")

    if choice == "5":
        employee.close()
        break
    elif choice == "1":
        name = input("Employee name: ")
        des = input("Employee designation: ")
        employee.insert(name, des)
    elif choice == "2":
        empid = input("Enter employee ID: ")
        employee.display(empid)
    elif choice == "3":
        empid = input("Enter employee ID to update: ")
        des = input("What is the new designation: ")
        employee.update(empid, des)
    elif choice == "4":
        empid = input("Enter the employee ID to delete: ")
        employee.delete(empid)
