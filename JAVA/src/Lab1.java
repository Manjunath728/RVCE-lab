import java.util.*;
class Person{
	String name,address,email_id,phoneno;
	public Person(String name,String address,String phoneno,String email_id) {
		this.name=name;
		this.address=address;
		this.email_id=email_id;
		this.phoneno=phoneno;
	}
	public void display() {
		System.out.println("Name : " +name);
		System.out.println("Address : " +address);
		System.out.println("Phone no : " +phoneno);
		System.out.println("Email ID : " +email_id);
	}
	
}
class Staff extends Person implements Staff_Op{
	String company,empid,designation;
	double salary;
	public Staff(String name,String address,String email_id,String phoneno,String company,String empid,String designation) {
		super(name,address,email_id,phoneno);
		this.company=company;
		this.empid=empid;
		this.designation=designation;		
	}
	public void display() {
		super.display();
		System.out.println("Company : " +this.company);
		System.out.println("Employee ID : " +this.empid);
		System.out.println("Designation : " +this.designation);
		System.out.println("Salary : " +this.salary);
	}
	public void cal_Salary(double sal) {
		this.salary+=(0.15*sal);
	}
}
class Student extends Person implements Student_Op{
	String USN,branch;
	int year;
	double fees;
	public Student(String name,String address,String email_id,String phoneno,String USN,String branch,int year) {
	super(name,address,email_id,phoneno);
	this.USN=USN;
	this.branch=branch;
	this.year=year;
	}
	public void display() {
		super.display();
		System.out.println("USN : " +USN);
		System.out.println("branch : " +branch);
		System.out.println("Year : " +year);
		System.out.println("Fees : " +fees);
	}
	public void cal_Fees(double fees) {
		this.fees+=(fees*0.15);
	}
}
interface Staff_Op{
	void cal_Salary(double sal);
	
}
interface Student_Op{
	void cal_Fees(double fees);
}

public class Lab1{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		Student s1=new Student("Kishore","Banglore","abc@gmail.com","7873683674","1RV22MC043","MCA",2022);
		System.out.println("Enter the Fees of the student : ");
		double fees=sc.nextDouble();
		s1.cal_Fees(fees);
		s1.display();
		
		Staff st1=new Staff("Kishore","Banglore","abc@gmail.com","7873683674","ABC","1001","Developer");
		System.out.println("Enter the Salary of the Employee : ");
		double sal=sc.nextDouble();
		st1.cal_Salary(sal);
		st1.display();
        sc.close();
	}
}