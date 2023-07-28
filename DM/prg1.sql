//craete tables

CREATE TABLE DEPARTMENT (
    dno VARCHAR(10),
    dname VARCHAR(255) not null,
    primary key(dno)
);

CREATE TABLE PROJECT (
    pname varchar(255) not null,
    pno varchar(10),
    ploc varchar(255),
    dno varchar(10),
    primary key (pno),
    foreign key(dno) references DEPARTMENT(dno)
);

CREATE TABLE EMPLOYEE (
    essn varchar(10),
    fname varchar(255),
    mname varchar(255),
    lname varchar(255),
    bdate date,
    address varchar(255),
    gender varchar(6) not null,
    salary decimal(10,2),
    dno varchar(10),
    sssn varchar(10),
    primary key(essn),
    foreign key(dno) references DEPARTMENT(dno)
) ;
alter table EMPLOYEE add foreign key(sssn) references EMPLOYEE(essn);

create table DEPENDENT (
    dependentname varchar(30),
    relation varchar(20),
    dob date,
    essn varchar(10),
    primary key(dependentname,essn),
    foreign key(essn) references EMPLOYEE (essn)
);

create table WORK (
    essn varchar(10),
    pno varchar(10),
    hour int ,
    weekno int,
    primary key(essn,pno,weekno),
    foreign key(essn) references EMPLOYEE (essn),
    foreign key(pno) references PROJECT (pno)
);
create table LOCATION (
    dno varchar(10),
    dloc varchar(100),
    primary key(dno,dloc),
    foreign key(dno) references DEPARTMENT(dno)
);
create table MANAGER(
    managerssn varchar(10),
    dno varchar(10),
    managerstart date,
    primary key(managerssn,managerstart,dno),
    foreign key(managerssn) references EMPLOYEE(essn),
    foreign key(dno) references DEPARTMENT(dno)
);


1)

SELECT E.fname AS f_Name, E.lname AS l_Name, D.dname AS dept_Name
FROM EMPLOYEE E
JOIN DEPARTMENT D ON E.dno = D.dno
WHERE E.salary > (
    SELECT AVG(salary) 
    FROM EMPLOYEE 
    WHERE dno = 'D006' -- 'D006' is the department number for the Finance department
);

2)
SELECT E.essn, E.fname AS f_Name, E.lname AS l_Name, D.dname AS dept_Name
FROM EMPLOYEE E
JOIN DEPARTMENT D ON E.dno = D.dno
WHERE E.essn IN (
    SELECT essn
    FROM WORK
    WHERE pno IN (
        SELECT pno
        FROM PROJECT
        WHERE dno = 'D007'
    )
    GROUP BY essn
    HAVING COUNT(DISTINCT pno) > 2
);
3)

SELECT P.pname AS project_name, P.pno AS project_number, P.ploc AS project_location, D.dname AS department_name
FROM PROJECT P
JOIN DEPARTMENT D ON P.dno = D.dno
WHERE P.pno IN (
    SELECT pno
    FROM WORK
); b  