/* CREATE TABLE EMPLOYEEDETAILS (
    EMP_ID VARCHAR(10) NOT NULL,
    FULL_NAME VARCHAR(20) NOT NULL,
    MANAGER_ID INT,
    DATE_OF_JOINING DATE NOT NULL,
    CITY VARCHAR(20) NOT NULL
);

INSERT INTO EMPLOYEEDETAILS VALUES
('123', 'SHASHI RANJAN', 12, '2024-09-15', 'HYDERABAD'),
('124', 'ANUJ SINGH', 12, '2024-12-17', 'PUNE'),
('113', 'GANESH TIWARI', 12, '2021-04-5', 'BENGALURU'),
('125', 'BRAJESH PATHAK ', 12, '2023-11-19', 'KOCHI'),
('129', 'RANJAN MISHRA', 12, '2024-09-17', 'HYDERABAD');

DELETE FROM EMPLOYEEDETAILS
WHERE FULL_NAME = 'SHASHI'; 


-- SHOW ALL THE RECORDS
SELECT * FROM EMPLOYEEDETAILS

-- SHOW THE EMPLOYEE WITH HYDERABAD LOCATION
SELECT * FROM  EMPLOYEEDETAILS WHERE CITY= 'HYDERABAD'

CREATE TABLE EMPLOYEE_SALARY
(
EMP_ID VARCHAR(10) NOT NULL, 
PROJECT VARCHAR(20) NOT NULL,
SALARY INT,
VARIABLE INT );

INSERT INTO EMPLOYEE_SALARY VALUES ( '123','P1',80000,10000),
('124','P3',50000,8000),
('113','P3',30000,5000),
('125','P3',40000,5000),
('129','P3',20000,1000)

--WRITE AN SQL QUERY TO FETCH ALL RECORDS IN BOTH TABLE 

SELECT * FROM EMPLOYEEDETAILS
SELECT * FROM EMPLOYEE_SALARY

-- MERGE BOTH TABLE 
SELECT ED.*, ES.PROJECT, ES.SALARY, ES.VARIABLE
FROM EMPLOYEEDETAILS ED
INNER JOIN EMPLOYEE_SALARY ES ON ED.EMP_ID = ES.EMP_ID;

-- INSERT MORE ROWS INTO THE TABLE EMPLOYEE_DETAILS
INSERT INTO EMPLOYEEDETAILS (EMP_ID, FULL_NAME, MANAGER_ID, DATE_OF_JOINING, CITY) VALUES
('130', 'PRIYA SINGH', 12, '2024-06-25', 'MUMBAI'),
('131', 'RAJESH KUMAR', 12, '2024-03-10', 'DELHI'),
('140','RAKESH SAW',15,'2024-01-6','KOLKATA'),
('147','RAMESH BANARJEE',41,'2022-07-23','NOIDA');

-- ARRANGE THE RECORDS ACCORDING TO DATE OF JOINING.

SELECT * FROM EMPLOYEEDETAILS ORDER BY DATE_OF_JOINING

-- ARRANGE THE RECORDS ACCORDING TO THE CITY NAME

SELECT *FROM EMPLOYEEDETAILS ORDER BY DATE_OF_JOINING ASC;

-- ARRANGE THE RECORDS ACCORDING TO THE EMPLOYEE_ID DETAILS


 SELECT * FROM EMPLOYEE_SALARY ORDER BY EMP_ID ASC

 -- INSERT THE DATA INTO EMPLOYEE_SALARY
 INSERT INTO EMPLOYEE_SALARY VALUES 
('130','P7',25000,8000),
('131','P9',20000,5000),
('140','P4',40000,5000),
('147','P10',20000,1000)

-- INSERT THE DATA INTO EMPLOYEEDETAILS AND EMPLOYEE_SALARY 

INSERT INTO EMPLOYEEDETAILS VALUES 
('156','DENESH KUMAR',15,'2020-04-13','PUNE'),
('196','MANISH KUMAR',15,'2020-11-16','HYDERABAD'),
('167','GANESH',51,'2023-10-23','DELHI');

INSERT INTO EMPLOYEE_SALARY VALUES
('156','P6',45000,5000),
('196','P6',45000,10000),
('167','P2',35000,1000);

-- FATCH ALL THE DATA WHERE CITY NAME IS HYDERABAD

SELECT * FROM EMPLOYEEDETAILS WHERE CITY= 'HYDERABAD'

-- FATCH ALL THE DATA WHERE MANAGER ID IS 12 AND CITY NAME IS HYDERABAD

SELECT * FROM EMPLOYEEDETAILS WHERE MANAGER_ID = 12 AND CITY='HYDERABAD'

-- WRITE AN SQL QUERY TO FATCH THE DATA AND COUNT OF EMPLOYEE WORKING IN PROJECT P1

SELECT COUNT(*) FROM EMPLOYEE_SALARY WHERE PROJECT IN  ('P2','P3')

-- SHOW ALL THE DETAILS FROM EMPLOYEE_SALARY.

SELECT * FROM EMPLOYEE_SALARY

-- ALTER THE EMPLOYEE_DETAILS 
ALTER TABLE EMPLOYEEDETAILS ADD [GENDER ]VARCHAR(10);

SELECT * FROM EMPLOYEEDETAILS

-- SET GENDER INTO MALE IN ALL THE ROWS .
UPDATE EMPLOYEEDETAILS SET GENDER= 'MALE';

-- SET GENDER INTO FEMALE IN EVERY 2ND ROWS OF THE DATA


WITH NumberedRows AS (
    SELECT *, ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS RowNum
    FROM EMPLOYEEDETAILS
)
UPDATE NumberedRows
SET GENDER = 'FEMALE'
WHERE RowNum  = 1;

-- Displaying updated records
SELECT * FROM EMPLOYEEDETAILS;

-- WRITE SQL QUERY THAT TO FIND THE EMPLOYEE ID WHOSE SALARY LIES IN THE RANGE OF 45000 TO 60000.

SELECT * FROM EMPLOYEE_SALARY WHERE SALARY BETWEEN 45000 AND 60000


-- WRITE SQL QUERY TO FETCH THE EMPLOYEE DETAILS WHO WORK ON PRJECT OTHER THEN P2.


SELECT * FROM EMPLOYEE_SALARY WHERE NOT PROJECT='P2'

-- WRITE SQL QUERY TO UPDATE A ROW 

ALTER TABLE EMPLOYEE_SALARY DROP  COLUMN VARIABLE

SELECT * FROM EMPLOYEE_SALARY




SELECT COUNT(*)
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'dbo';

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'dbo';




-- CREATE TABLE AND ADDING DATA 


CREATE TABLE CorporateEmployees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Position VARCHAR(50),
    Salary DECIMAL(10, 2),
    HireDate DATE
);

INSERT INTO CorporateEmployees VALUES
(1, 'John', 'Doe', 'Finance', 'Accountant', 60000.00, '2023-01-05'),
(2, 'Jane', 'Smith', 'Human Resources', 'HR Manager', 75000.00, '2022-07-15'),
(3, 'Michael', 'Johnson', 'Marketing', 'Marketing Analyst', 55000.00, '2023-03-20'),
(4, 'Emily', 'Williams', 'Operations', 'Operations Manager', 80000.00, '2021-11-10'),
(5, 'David', 'Brown', 'IT', 'Systems Administrator', 65000.00, '2022-02-28'),
(6, 'Jessica', 'Davis', 'Finance', 'Financial Analyst', 62000.00, '2022-09-18'),
(7, 'Daniel', 'Miller', 'Human Resources', 'Recruiter', 58000.00, '2023-05-12'),
(8, 'Sarah', 'Wilson', 'Marketing', 'Marketing Coordinator', 50000.00, '2023-08-07'),
(9, 'Matthew', 'Moore', 'IT', 'Software Engineer', 70000.00, '2022-04-30'),
(10, 'Amanda', 'Taylor', 'Operations', 'Supply Chain Analyst', 57000.00, '2021-12-22'),
(11, 'Christopher', 'Anderson', 'Finance', 'Financial Controller', 90000.00, '2022-06-08'),
(12, 'Ashley', 'Martinez', 'Human Resources', 'Training Coordinator', 58000.00, '2023-02-14'),
(13, 'James', 'Hernandez', 'Marketing', 'Marketing Manager', 75000.00, '2021-10-25'),
(14, 'Jennifer', 'Garcia', 'IT', 'Network Administrator', 68000.00, '2022-03-15'),
(15, 'Robert', 'Young', 'Operations', 'Operations Coordinator', 60000.00, '2023-04-02'),
(16, 'Stephanie', 'Lopez', 'Finance', 'Finance Manager', 85000.00, '2022-08-12'),
(17, 'William', 'Gonzalez', 'Human Resources', 'HR Assistant', 52000.00, '2023-06-30'),
(18, 'Kimberly', 'Perez', 'Marketing', 'Digital Marketing Specialist', 53000.00, '2023-09-19'),
(19, 'Joseph', 'Robinson', 'IT', 'Database Administrator', 72000.00, '2022-05-10'),
(20, 'Megan', 'Lewis', 'Operations', 'Operations Analyst', 62000.00, '2021-12-01'),
(21, 'Jonathan', 'Walker', 'Finance', 'Financial Analyst', 60000.00, '2022-11-28'),
(22, 'Samantha', 'Hill', 'Human Resources', 'Compensation Analyst', 57000.00, '2023-03-10'),
(23, 'Nicholas', 'Scott', 'Marketing', 'Content Writer', 48000.00, '2023-07-05'),
(24, 'Olivia', 'Green', 'IT', 'Security Analyst', 69000.00, '2022-09-20'),
(25, 'Benjamin', 'Adams', 'Operations', 'Quality Assurance Specialist', 61000.00, '2023-01-18'),
(26, 'Victoria', 'Baker', 'Finance', 'Finance Assistant', 55000.00, '2022-04-12'),
(27, 'Samuel', 'Rivera', 'Human Resources', 'Benefits Coordinator', 59000.00, '2023-08-25'),
(28, 'Lauren', 'Torres', 'Marketing', 'Social Media Coordinator', 51000.00, '2023-12-03'),
(29, 'Christopher', 'Lee', 'IT', 'IT Support Specialist', 64000.00, '2022-06-16'),
(30, 'Melissa', 'Wright', 'Operations', 'Logistics Coordinator', 58000.00, '2021-11-14');


select * from CorporateEmployees

UPDATE  CorporateEmployees SET  Salary= 65000, DEPARTMENT = 'Finance' WHERE EmployeeID=1

UPDATE CorporateEmployees 
SET LastName = 'Jones', Department = 'Operations' 
WHERE EmployeeID = 15;

DELETE FROM CorporateEmployees WHERE EmployeeID=30

INSERT INTO CorporateEmployees VALUES(30,'Nik','Jones','IT','Systems Administrator',65000,'2023-04-11')



CREATE TABLE DEPARTMENT (
    DEPTID CHAR(5) PRIMARY KEY,
    DEPTNAME VARCHAR(50) NOT NULL,
    MGRID CHAR(5),
    LOCATION_ID CHAR(5));

CREATE TABLE EMPLOYEES (
    EMP_ID CHAR(5) PRIMARY KEY,
    FIRST_NAME VARCHAR(50) NOT NULL,
    LAST_NAME VARCHAR(50) NOT NULL,
    EMAIL VARCHAR(100),
    PHONE_NUMBER VARCHAR(20),
    DEPTID CHAR(5),
    MGRID CHAR(5),
    COMMISSION DECIMAL(10,2),
    SALARY DECIMAL(10,2),
    JOB_ID INT,
    HIRE_DATE DATE,
    FOREIGN KEY (DEPTID) REFERENCES DEPARTMENT(DEPTID)
);

CREATE TABLE JOBS (
    JOB_ID INT PRIMARY KEY,
    JOB_TITLE VARCHAR(50),
    MIN_SALARY DECIMAL(10,2)
);

CREATE TABLE LOCATION (
    LOCATION_ID CHAR(5) PRIMARY KEY,
    STREET_ADDRESS VARCHAR(100),
    POSTAL_CODE VARCHAR(20),
    CITY VARCHAR(50),
    STATE_PROVINCE VARCHAR(50),
    COUNTRY_ID CHAR(2)
);

CREATE TABLE JOB_HISTORY (
    EMP_ID CHAR(5),
    START_DTE DATE,
    END_DTE DATE,
    JOB_ID INT,
    DEPT_ID CHAR(5),
    FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEES(EMP_ID),
    FOREIGN KEY (JOB_ID) REFERENCES JOBS(JOB_ID),
    FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT(DEPTID)
);

-- Insert data into DEPARTMENT table
INSERT INTO DEPARTMENT (DEPTID, DEPTNAME, MGRID, LOCATION_ID)
VALUES
('D001', 'HR', 'M001', 'L001'),
('D002', 'Finance', 'M002', 'L002'),
('D003', 'Marketing', 'M003', 'L003');


INSERT INTO DEPARTMENT (DEPTID, DEPTNAME, MGRID, LOCATION_ID)
VALUES
('D004','HR','M004','L004'),
('D005','Marketing','M005','L005');





-- Insert data into EMPLOYEES table
INSERT INTO EMPLOYEES (EMP_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, DEPTID, MGRID, COMMISSION, SALARY, JOB_ID, HIRE_DATE)
VALUES
('E001', 'John', 'Doe', 'john@example.com', '1234567890', 'D001', 'M001', NULL, 60000, 1, '2022-01-15'),
('E002', 'Jane', 'Smith', 'jane@example.com', '2345678901', 'D002', 'M002', NULL, 55000, 2, '2022-02-20'),
('E003', 'Michael', 'Johnson', 'michael@example.com', '3456789012', 'D003', 'M003', NULL, 52000, 3, '2022-03-25');

INSERT INTO EMPLOYEES (EMP_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, DEPTID, MGRID, COMMISSION, SALARY, JOB_ID, HIRE_DATE)
VALUES
('E004','FLIX','GIN','FLIX@gmail.com','9608348909','D004','M004',NULL,'72000',4,'2023-03-23'),
('E005','ARJU','SINGH','ARJU@gmail.com','9050340238','D005','M005',NULL,'80000',5,'2023-05-16');



-- Insert data into JOBS table
INSERT INTO JOBS (JOB_ID, JOB_TITLE, MIN_SALARY)
VALUES
(1, 'Manager', 50000),
(2, 'Developer', 40000),
(3, 'Accountant', 45000);

INSERT INTO JOBS(JOB_ID,JOB_TITLE,MIN_SALARY)
VALUES
(4,'Manager',35000),
(5,'Accountant',65000);

-- Insert data into LOCATION table
INSERT INTO LOCATION (LOCATION_ID, STREET_ADDRESS, POSTAL_CODE, CITY, STATE_PROVINCE, COUNTRY_ID)
VALUES
('L001', '123 Main St', '12345', 'New York', 'NY', 'US'),
('L002', '456 Queen St', '45678', 'Toronto', 'ON', 'CA'),
('L003', '789 King St', '78901', 'London', NULL, 'UK');

INSERT INTO LOCATION (LOCATION_ID,STREET_ADDRESS,POSTAL_CODE,CITY,STATE_PROVINCE,COUNTRY_ID)
VALUES
('L004','RANCHI','834009','RANCHI CITY','RNC','IND'),
('L005','PATNA','834010','PATNA CITY','PNBE','INDIA');




-- Insert data into JOB_HISTORY table
INSERT INTO JOB_HISTORY (EMP_ID, START_DTE, END_DTE, JOB_ID, DEPT_ID)
VALUES
('E001', '2022-01-15', NULL, 1, 'D001'),
('E002', '2022-02-20', NULL, 2, 'D002'),
('E003', '2022-03-25', NULL, 3, 'D003');

INSERT INTO JOB_HISTORY(EMP_ID,START_DTE,END_DTE,JOB_ID,DEPT_ID)
VALUES
('E004','2023-03-17',NULL,4,'D004'),
('E005','2022-04-15',NULL,5,'D005');




--SELECT * FROM LOCATION WHERE LOCATION_ID = 'L001 '
--SELECT * FROM EMPLOYEES WHERE EMP_ID = 'E001'

SELECT 
    e.EMP_ID,
    e.FIRST_NAME,
    e.LAST_NAME,
    e.EMAIL,
    e.PHONE_NUMBER,
    e.DEPTID,
    d.DEPTNAME,
    d.MGRID AS DEPT_MANAGER_ID,
    d.LOCATION_ID,
    l.STREET_ADDRESS,
    l.POSTAL_CODE,
    l.CITY,
    l.STATE_PROVINCE,
    l.COUNTRY_ID,
    e.MGRID AS EMP_MANAGER_ID,
    e.COMMISSION,
    e.SALARY,
    j.JOB_ID,
    j.JOB_TITLE,
    j.MIN_SALARY AS JOB_MIN_SALARY,
    e.HIRE_DATE,
    jh.START_DTE AS JOB_START_DATE,
    jh.END_DTE AS JOB_END_DATE
FROM 
    EMPLOYEES e
JOIN 
    DEPARTMENT d ON e.DEPTID = d.DEPTID
JOIN 
    LOCATION l ON d.LOCATION_ID = l.LOCATION_ID
JOIN 
    JOBS j ON e.JOB_ID = j.JOB_ID
LEFT JOIN 
    JOB_HISTORY jh ON e.EMP_ID = jh.EMP_ID








INSERT INTO DEPARTMENT (DEPTID, DEPTNAME, MGRID, LOCATION_ID)
VALUES
('D004','HR','M004','L004'),
('D005','Marketing','M005','L005');



INSERT INTO EMPLOYEES (EMP_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, DEPTID, MGRID, COMMISSION, SALARY, JOB_ID, HIRE_DATE)
VALUES
('E004','FLIX','GIN','FLIX@gmail.com','9608348909','D004','M004',NULL,'72000',4,'2023-03-23'),
('E005','ARJU','SINGH','ARJU@gmail.com','9050340238','D005','M005',NULL,'80000',5,'2023-05-16');


INSERT INTO JOBS(JOB_ID,JOB_TITLE,MIN_SALARY)
VALUES
(4,'Manager',35000),
(5,'Accountant',65000);

INSERT INTO LOCATION (LOCATION_ID,STREET_ADDRESS,POSTAL_CODE,CITY,STATE_PROVINCE,COUNTRY_ID)
VALUES
('L004','RANCHI','834009','RANCHI CITY','RNC','BH'),
('L005','PATNA','834010','PATNA CITY','PNBE','GY');

INSERT INTO JOB_HISTORY(EMP_ID,START_DTE,END_DTE,JOB_ID,DEPT_ID)
VALUES
('E004','2023-03-17',NULL,4,'D004'),
('E005','2022-04-15',NULL,5,'D005');



CREATE TABLE STUDENT
( 
STUDENT_NAME VARCHAR(20) NOT NULL,
STUDENT_CLASS INT  NOT NULL,
STUDENT_ROLL INT NOT NULL,
STUDENT_FATHER_NAME VARCHAR(30),
STUDENT_MOTHER_NAME VARCHAR(30),
STUDENT_ADDRESS VARCHAR(50));

INSERT INTO STUDENT ( STUDENT_NAME,STUDENT_CLASS,STUDENT_ROLL,STUDENT_FATHER_NAME,STUDENT_MOTHER_NAME,STUDENT_ADDRESS) VALUES 
( 'ARJUN','5','12','NITESH SINGH','NILAM SINGH','AURANGABAD'),
( 'ARUN SAW','5','12','NITESH SAW','NILAM SAW','RAIPUR');


INSERT INTO STUDENT ( STUDENT_NAME,STUDENT_CLASS,STUDENT_ROLL,STUDENT_FATHER_NAME,STUDENT_MOTHER_NAME,STUDENT_ADDRESS) VALUES 
('Ravi Shankar', '10', '101', 'Gopal Shankar', 'Lakshmi Shankar', 'Chennai, Tamil Nadu'),
('Priya Menon', '9', '102', 'Rajesh Menon', 'Meera Menon', 'Bangalore, Karnataka'),
('Sanjay Kumar', '11', '103', 'Rajendra Kumar', 'Anita Kumar', 'Hyderabad, Telangana'),
('Divya Nair', '8', '104', 'Suresh Nair', 'Rekha Nair', 'Kochi, Kerala'),
('Saranya Balan', '12', '105', 'Arvind Balan', 'Priya Balan', 'Coimbatore, Tamil Nadu'),
('Vijay Prasad', '10', '106', 'Ramesh Prasad', 'Sujatha Prasad', 'Mysore, Karnataka'),
('Meenakshi Venkat', '9', '107', 'Venkatraman Iyer', 'Lakshmi Venkat', 'Pondicherry, Tamil Nadu'),
('Rajesh Pillai', '11', '108', 'Anand Pillai', 'Shanthi Pillai', 'Trivandrum, Kerala'),
('Anusha Rao', '8', '109', 'Ravi Rao', 'Shobha Rao', 'Vishakhapatnam, Andhra Pradesh'),
('Arjun Reddy', '12', '110', 'Rajendra Reddy', 'Latha Reddy', 'Bengaluru, Karnataka');

-- ADDING COLUMN INTO THE TABLE.
ALTER TABLE STUDENT 
ADD  STUDENT_ADDRESS VARCHAR (50);

-- DROP  COLUMN FROM TABLE.
ALTER TABLE STUDENT DROP COLUMN STUDENT_ADDRESS


--  WRITE SQL QUERY FOR DELETE TABLE  
DROP TABLE STUDENT


-- THIS QUERY FOR FETCH ALL THE DATA IN TABLE

SELECT * FROM STUDENT

-- WRITE QUEERY FOR DELETE A ROWS OF DATA 

DELETE FROM STUDENT WHERE STUDENT_ADDRESS = 'AURANGABAD' ;

INSERT INTO STUDENT  (STUDENT_NAME,STUDENT_CLASS,STUDENT_ROLL,STUDENT_FATHER_NAME,STUDENT_MOTHER_NAME,STUDENT_ADDRESS) VALUES
('MANOJ','3','12','GOVIND GIRI','LAKSHMI','HYDERABAD'),
('MANOJ','3','12','MAHENDR','MAHALAKSHMI','CHENNAI');


CREATE TABLE STATE ( 
State_name varchar(20),
State_code varchar(5),
State_population bigint,
state_capital varchar (20));




INSERT INTO STATE(State_name, State_code, State_population, state_capital) 
VALUES 
('KARNATAKA', 4, 154584000, 'BENGALURU'),
('MAHARASHTRA', 5, 122153000 ,'MUMBAI'),
('UTTAR PRADESH', 6, 234567000, 'LUCKNOW'),
('TAMIL NADU', 7, 78115600, 'CHENNAI'),
('ANDHRA PRADESH', 8, 53903300,  'AMARAVATI'),
('WEST BENGAL', 9, 96906000,  'KOLKATA'),
('GUJARAT', 10, 67936000, 'GANDHINAGAR'),
('RAJASTHAN', 11, 68936900,'JAIPUR'),
('MADHYA PRADESH', 12, 82232000, 'BHOPAL'),
('BIHAR', 13, 124799000, 'PATNA');

SELECT * FROM STATE


ALTER TABLE STATE ADD STATE_DEVLOPMENT_INDEX INT


ALTER TABLE STATE DROP COLUMN STATE_DEVLOPMENT_INDEX;


INSERT INTO STATE(State_name,State_code,State_population,state_capital) VALUES
('JHARKHAND',28,53455349,'RANCHI');

DROP TABLE STATE


CREATE TABLE SONG
(
SONG_ID INT,
TITLE VARCHAR(100),
ARTIST VARCHAR(100),
ALBUM VARCHAR(100),
RELEASE_YEAR DATE,
DURATION TIME,
);

INSERT INTO SONG( SONG_ID,TITLE,ARTIST,ALBUM,RELEASE_YEAR,DURATION) VALUES
(12,'CHAP DHAN HO','PAWAN SINGH',NULL,'2024-04-19','03:51:00');

SELECT * FROM SONG

INSERT INTO SONG( SONG_ID,TITLE,ARTIST,ALBUM,RELEASE_YEAR,DURATION) VALUES
(13,'PIYA CHODD DIHI N','PAWAN SINGH',NULL,'2024-05-11','03:11:00'),
(14,'TIKULIYA','PAWAN SINGH',NULL,'2024-02-14','03:28:00');

-- DISCRIBE COMMAND FOR SONG TABLE 

EXEC sp_columns 'Song';


-- 
CREATE TABLE "Departments" (
    "dept_no" VARCHAR(4)   NOT NULL,
    "dept_name" VARCHAR(50)   NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE "Dept_Emp" (
    "emp_no" INT   NOT NULL,
    "dept_no" VARCHAR(4)   NOT NULL,
    CONSTRAINT "pk_Dept_Emp" PRIMARY KEY (
        "emp_no","dept_no"
     )
);

CREATE TABLE "Dept_Manager" (
    "dept_no" VARCHAR(4)   NOT NULL,
    "emp_no" INT   NOT NULL,
    CONSTRAINT "pk_Dept_Manager" PRIMARY KEY (
        "dept_no","emp_no"
     )
);

CREATE TABLE "Employees" (
    "emp_no" INT   NOT NULL,
    "emp_title_id" VARCHAR(5)   NOT NULL,
    "birth_date" DATE   NOT NULL,
    "first_name" VARCHAR(50)   NOT NULL,
    "last_name" VARCHAR(50)   NOT NULL,
    "sex" VARCHAR(1)   NOT NULL,
    "hire_date" DATE   NOT NULL,
    CONSTRAINT "pk_Employees" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "Salaries" (
    "emp_no" INT   NOT NULL,
    "salary" INT   NOT NULL,
    CONSTRAINT "pk_Salaries" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "Titles" (
    "title_id" VARCHAR(5)   NOT NULL,
    "title" VARCHAR(50)   NOT NULL,
    CONSTRAINT "pk_Titles" PRIMARY KEY (
        "title_id"
     )
);-- Insert data into Departments
INSERT INTO Departments ("dept_no", "dept_name")
VALUES ('d001', 'Marketing'),
       ('d002', 'Finance'),
       ('d003', 'Human Resources'),
       ('d004', 'Production'),
       ('d005', 'Development'),
       ('d006', 'Quality Management'),
       ('d007', 'Sales'),
       ('d008', 'Research'),
       ('d009', 'Customer Service'),
       ('d010', 'Legal');

-- Insert data into Dept_Emp
INSERT INTO Dept_Emp ("emp_no", "dept_no")
VALUES (10001, 'd005'),
       (10002, 'd003'),
       (10003, 'd004'),
       (10004, 'd004'),
       (10005, 'd008'),
       (10006, 'd005'),
       (10007, 'd005'),
       (10008, 'd005'),
       (10009, 'd005'),
       (10010, 'd005');

-- Insert data into Dept_Manager
INSERT INTO Dept_Manager ("dept_no", "emp_no")
VALUES ('d001', 10001),
       ('d002', 10002),
       ('d003', 10003),
       ('d004', 10004),
       ('d005', 10005),
       ('d006', 10006),
       ('d007', 10007),
       ('d008', 10008),
       ('d009', 10009),
       ('d010', 10010);

-- Insert data into Employees
INSERT INTO Employees ("emp_no", "emp_title_id", "birth_date", "first_name", "last_name", "sex", "hire_date")
VALUES (10001, 'e0001', '1973-09-02', 'Georgi', 'Facello', 'M', '1986-06-26'),
       (10002, 'e0002', '1964-06-02', 'Bezalel', 'Simmel', 'F', '1985-11-21'),
       (10003, 'e0003', '1959-12-03', 'Parto', 'Bamford', 'M', '1986-08-28'),
       (10004, 'e0004', '1954-05-01', 'Chirstian', 'Koblick', 'M', '1986-12-01'),
       (10005, 'e0005', '1955-01-21', 'Kyoichi', 'Maliniak', 'M', '1989-09-12'),
       (10006, 'e0006', '1953-04-20', 'Anneke', 'Preusig', 'F', '1989-06-02'),
       (10007, 'e0007', '1957-05-23', 'Tzvetan', 'Zielinski', 'F', '1989-02-10'),
       (10008, 'e0008', '1958-02-19', 'Saniya', 'Kalloufi', 'M', '1994-09-15'),
       (10009, 'e0009', '1952-04-19', 'Sumant', 'Peac', 'F', '1985-02-18'),
       (10010, 'e0010', '1963-06-01', 'Duangkaew', 'Piveteau', 'F', '1989-08-24');

-- Insert data into Salaries
INSERT INTO Salaries ("emp_no", "salary")
VALUES (10001, 60117),
       (10002, 65828),
       (10003, 40006),
       (10004, 40054),
       (10005, 78228),
       (10006, 40000),
       (10007, 56724),
       (10008, 46671),
       (10009, 60929),
       (10010, 72488);

-- Insert data into Titles
INSERT INTO Titles ("title_id", "title")
VALUES ('e0001', 'Senior Engineer'),
       ('e0002', 'Staff'),
       ('e0003', 'Engineer'),
       ('e0004', 'Senior Staff'),
       ('e0005', 'Assistant Engineer'),
       ('e0006', 'Technique Leader'),
       ('e0007', 'Manager');



-- BASIC SQL COMMANDS 
SELECT dept_name  DEPART_NAME,first_name NAME,last_name SURNAME,birth_date  DATE_OF_BIRTH FROM Departments , Employees,Dept_Emp,Dept_Manager


-- TO ELIMINATE THE DUBLICATES ROWS 
SELECT DISTINCT emp_title_id,first_name FROM Employees

-- TO FETCH THE UNIQUE ROW 
select  emp_title_id,first_name FROM Employees



DROP TABLE Employees
CREATE TABLE EMPLOYEES( 
EMP_ID VARCHAR(5) NOT NULL,
EMP_FIRST_NAME VARCHAR(20) NOT NULL,
EMP_LAST_NAME VARCHAR(15) NOT NULL,
EMP_SALARY DECIMAL NOT NULL,
EMP_DEPARTMENT VARCHAR(20) NOT NULL 
);


INSERT INTO EMPLOYEES (EMP_ID, EMP_FIRST_NAME, EMP_LAST_NAME, EMP_SALARY, EMP_DEPARTMENT)
VALUES 
('10001', 'John', 'Doe', 50000, 'Marketing'),
('10002', 'Jane', 'Smith', 60000, 'Finance'),
('10003', 'Michael', 'Johnson', 55000, 'HR'),
('10004', 'Emily', 'Brown', 52000, 'Marketing'),
('10005', 'David', 'Williams', 58000, 'Finance'),
('10006', 'Sarah', 'Jones', 53000, 'HR'),
('10007', 'Chris', 'Wilson', 51000, 'Marketing'),
('10008', 'Jessica', 'Martinez', 59000, 'Finance'),
('10009', 'Matthew', 'Taylor', 54000, 'HR'),
('10010', 'Laura', 'Anderson', 57000, 'Marketing');

-- ARTHMATIC OPERATION
SELECT EMP_ID,EMP_SALARY, EMP_SALARY*12 AS ANNUAL_SALARY FROM EMPLOYEES

-- ARTHMETIC EXPRESSION AND NULL VALUES

SELECT EMP_ID,(EMP_SALARY+14000)*12 AS ANNUAL_SALARY FROM EMPLOYEES



-- WHERE CLAUSE

SELECT * FROM EMPLOYEES WHERE EMP_ID = '10008'

SELECT * FROM EMPLOYEES WHERE EMP_DEPARTMENT= 'HR'

SELECT * FROM EMPLOYEES WHERE EMP_SALARY >55000

-- BETWEEN , AND OPERATOR

SELECT * FROM EMPLOYEES WHERE EMP_SALARY BETWEEN '40000' AND '57000'

SELECT * FROM EMPLOYEES WHERE EMP_ID BETWEEN '10006' AND '10009'

-- IN OPERATOR 

SELECT * FROM EMPLOYEES WHERE EMP_SALARY IN ( 54000,53000);

SELECT * FROM EMPLOYEES WHERE EMP_SALARY = '52000'

INSERT INTO EMPLOYEES (EMP_ID, EMP_FIRST_NAME, EMP_LAST_NAME, EMP_SALARY, EMP_DEPARTMENT) 
VALUES
(1, 'Suresh', 'Kumar', 50000, 'Engineering'),
(2, 'Priya', 'Raj', 55000, 'Marketing'),
(3, 'Arjun', 'Menon', 60000, 'Finance'),
(4, 'Deepa', 'Nair', 52000, 'Human Resources'),
(5, 'Ganesh', 'Iyer', 58000, 'Sales'),
(6, 'Anjali', 'Chandran', 53000, 'Engineering'),
(7, 'Ravi', 'Pillai', 56000, 'Marketing'),
(8, 'Meera', 'Nair', 59000, 'Finance'),
(9, 'Karthik', 'Nair', 54000, 'Human Resources'),
(10, 'Shalini', 'Menon', 57000, 'Sales');



SELECT * FROM EMPLOYEES WHERE EMP_SALARY IN (50000,58000)

SELECT * FROM EMPLOYEES WHERE EMP_ID BETWEEN  1 AND 10008

SELECT * FROM EMPLOYEES WHERE EMP_DEPARTMENT= 'Human Resources'



--Q1 Retrieve all columns for employees whose salary is greater than 55000.

SELECT * FROM EMPLOYEES WHERE EMP_SALARY > 55000

--Q2 Display the first name and last name of employees who work in the Marketing department.

SELECT EMP_FIRST_NAME,  EMP_LAST_NAME FROM EMPLOYEES WHERE EMP_DEPARTMENT = 'Marketing'

-- Q3 List the employee ID and salary of employees working in the Finance department.

SELECT EMP_ID , EMP_SALARY FROM EMPLOYEES WHERE EMP_DEPARTMENT= 'Finance'

--Q4. Count the number of employees in each department

--Q5  Calculate the average salary of employees in the HR department

SELECT AVG(EMP_SALARY) AS avg_salary FROM EMPLOYEES WHERE EMP_DEPARTMENT = 'HR'

-- Q6 Find the maximum salary among all employees

SELECT MAX(EMP_SALARY) FROM EMPLOYEES

-- Q7 Retrieve the employee with the highest salary

SELECT * FROM EMPLOYEES WHERE EMP_SALARY= ( SELECT MAX(EMP_SALARY) FROM EMPLOYEES);

--Q8. Calculate the total salary expense for the company

SELECT  SUM (EMP_SALARY) AS EMP FROM EMPLOYEES

-- Q9. Display the first name, last name, and salary of employees in descending order of salary


--10 Find the department with the highest average salary







-- IS NULL OPERATOR

SELECT * FROM EMPLOYEES WHERE EMP_ID IS NULL

SELECT * FROM EMPLOYEES WHERE EMP_ID IS NOT NULL


-- LOGICAL OPERATOR


SELECT * FROM EMPLOYEES WHERE EMP_SALARY >55000 AND EMP_SALARY < 60000

SELECT * FROM EMPLOYEES WHERE EMP_DEPARTMENT = 'HR'

SELECT * FROM EMPLOYEES WHERE EMP_FIRST_NAME = 'David'

SELECT * FROM EMPLOYEES WHERE EMP_SALARY >50000


SELECT * FROM EMPLOYEES WHERE EMP_DEPARTMENT = 'Marketing'

SELECT * FROM EMPLOYEES WHERE EMP_SALARY = 51000 




-- ORDER BY CLAUSE 


SELECT * FROM EMPLOYEES ORDER BY EMP_FIRST_NAME

SELECT * FROM EMPLOYEES ORDER BY EMP_DEPARTMENT DESC

SELECT * FROM EMPLOYEES ORDER BY EMP_DEPARTMENT DESC

SELECT * FROM EMPLOYEES ORDER BY EMP_LAST_NAME DESC

SELECT * FROM EMPLOYEES ORDER BY EMP_ID DESC

SELECT * FROM EMPLOYEES ORDER BY EMP_DEPARTMENT DESC 




-- ASC AND DESC Operators

SELECT * FROM EMPLOYEES ORDER BY EMP_FIRST_NAME ASC
SELECT * FROM EMPLOYEES ORDER BY EMP_LAST_NAME DESC,EMP_FIRST_NAME DESC 

SELECT * FROM EMPLOYEES ORDER BY EMP_FIRST_NAME DESC

SELECT * FROM EMPLOYEES ORDER BY EMP_SALARY DESC

SELECT * FROM EMPLOYEES ORDER BY EMP_SALARY ASC


-- NULLS FIRST AND NULLS LAST OPERATOR 

SELECT * FROM EMPLOYEES ORDER BY EMP_FIRST_NAME DESC 


-- ROWID AND ROWNUM

SELECT EMP_ID, EMP_FIRST_NAME FROM EMPLOYEES

-- FETCH CLAUSE

SELECT * FROM EMPLOYEES ORDER BY EMP_SALARY DESC OFFSET 1 ROW FETCH FIRST 10 ROWS ONLY


-- SINGLE ROW FUNCTION



CREATE TABLE Company (
    CompanyID INT PRIMARY KEY,
    CompanyName VARCHAR(100),
    Industry VARCHAR(100),
    Revenue DECIMAL(18, 2),
    EmployeeCount INT,
    CEOName VARCHAR(100),
    FoundedYear INT,
    HeadquartersCity VARCHAR(100),
    OfficeLocation VARCHAR(100),
    Website VARCHAR(255),
    ContactEmail VARCHAR(100)
);

-- Insert 50 rows of data with various office locations
INSERT INTO Company (CompanyID, CompanyName, Industry, Revenue, EmployeeCount, CEOName, FoundedYear, HeadquartersCity, OfficeLocation, Website, ContactEmail)
VALUES
    (1, 'ABC Corporation', 'Technology', 1000000.00, 50, 'John Doe', 1990, 'New York', 'Bengaluru', 'https://www.abccorp.com', 'contact@abccorp.com'),
    (2, 'XYZ Inc.', 'Finance', 750000.00, 30, 'Jane Smith', 1985, 'London', 'Hyderabad', 'https://www.xyzinc.com', 'info@xyzinc.com'),
    (3, '123 Industries', 'Manufacturing', 500000.00, 20, 'Mike Johnson', 2005, 'Los Angeles', 'Coimbatore', 'https://www.123industries.com', 'info@123industries.com'),
    (4, 'Tech Innovations', 'Technology', 1200000.00, 60, 'Sarah Johnson', 2000, 'San Francisco', 'Chennai', 'https://www.techinnovations.com', 'info@techinnovations.com'),
    (5, 'Globe Logistics', 'Transportation', 850000.00, 40, 'David Lee', 1995, 'Paris', 'Pune', 'https://www.globelogistics.com', 'contact@globelogistics.com'),
    (6, 'Sunrise Pharmaceuticals', 'Healthcare', 650000.00, 25, 'Emily Brown', 2010, 'Chicago', 'Visakhapatnam', 'https://www.sunrisepharmaceuticals.com', 'info@sunrisepharmaceuticals.com'),
    (7, 'Alpha Construction', 'Construction', 900000.00, 55, 'Michael Smith', 1980, 'Berlin', 'Jaipur', 'https://www.alphaconstruction.com', 'contact@alphaconstruction.com'),
    (8, 'Energy Solutions Ltd.', 'Energy', 1100000.00, 70, 'Karen Williams', 2008, 'Tokyo', 'Kochi', 'https://www.energysolutions.com', 'info@energysolutions.com'),
    (9, 'Swift Retailers', 'Retail', 780000.00, 45, 'Daniel Taylor', 1998, 'Sydney', 'Madurai', 'https://www.swiftretailers.com', 'contact@swiftretailers.com'),
    (10, 'Green Fields Agro', 'Agriculture', 600000.00, 35, 'Jessica Martinez', 2003, 'Mexico City', 'Trivandrum', 'https://www.greenfieldsagro.com', 'info@greenfieldsagro.com'),
    (11, 'DataTech Solutions', 'Information Technology', 1300000.00, 80, 'Steven Harris', 2005, 'Toronto', 'Chennai', 'https://www.datatechsolutions.com', 'info@datatechsolutions.com'),
    (12, 'Blue Ocean Consulting', 'Consulting', 950000.00, 50, 'Laura Rodriguez', 1997, 'Barcelona', 'Hyderabad', 'https://www.blueoceanconsulting.com', 'contact@blueoceanconsulting.com'),
    (13, 'Bright Minds Academy', 'Education', 700000.00, 30, 'Kevin Jones', 2015, 'New Delhi', 'Kolkata', 'https://www.brightmindsacademy.com', 'info@brightmindsacademy.com'),
    (14, 'AeroTech Solutions', 'Aerospace', 1400000.00, 90, 'Sophia Brown', 2006, 'Dubai', 'Coimbatore', 'https://www.aerotechsolutions.com', 'info@aerotechsolutions.com'),
    (15, 'Golden Harvest Foods', 'Food & Beverage', 880000.00, 60, 'Mark Anderson', 2002, 'Cairo', 'Bangalore', 'https://www.goldenharvestfoods.com', 'contact@goldenharvestfoods.com'),
    (16, 'TechWave Innovations', 'Technology', 1150000.00, 75, 'Rachel Clark', 2007, 'Mumbai', 'Chennai', 'https://www.techwaveinnovations.com', 'info@techwaveinnovations.com'),
    (17, 'Skyline Real Estate', 'Real Estate', 720000.00, 40, 'Andrew White', 1999, 'London', 'Hyderabad', 'https://www.skylinerealestate.com', 'info@skylinerealestate.com'),
    (18, 'Infinite Solutions', 'Consulting', 980000.00, 55, 'Emma Wilson', 2004, 'New York', 'Chennai', 'https://www.infinitesolutions.com', 'contact@infinitesolutions.com'),
    (19, 'Sunset Resorts', 'Hospitality', 750000.00, 45, 'James Lee', 1996, 'Las Vegas', 'Goa', 'https://www.sunsetresorts.com', 'info@sunsetresorts.com'),
    (20, 'Marine Dynamics', 'Maritime', 600000.00, 35, 'Olivia Taylor', 2012, 'Cape Town', 'Visakhapatnam', 'https://www.marinedynamics.com', 'contact@marinedynamics.com'),
    (21, 'VistaTech Solutions', 'Information Technology', 1250000.00, 85, 'Ryan Martinez', 2009, 'Dallas', 'Bengaluru', 'https://www.vistatechsolutions.com', 'info@vistatechsolutions.com'),
    (22, 'Golden Sands Resorts', 'Hospitality', 800000.00, 50, 'Isabella Garcia', 1990, 'Rio de Janeiro', 'Kochi', 'https://www.goldensandsresorts.com', 'info@goldensandsresorts.com'),
    (23, 'Global Logistics Inc.', 'Transportation', 1050000.00, 65, 'Nathan Johnson', 2003, 'Los Angeles', 'Mysore', 'https://www.globallogisticsinc.com', 'contact@globallogisticsinc.com'),
    (71, 'Brighter Solutions', 'Consulting', 850000.00, 55, 'Sophie Harris', 2008, 'Seattle', 'Chennai', 'https://www.brightersolutions.com', 'info@brightersolutions.com'),
    (72, 'TechPro Services', 'Information Technology', 1200000.00, 80, 'Benjamin Smith', 2010, 'San Jose', 'Hyderabad', 'https://www.techproservices.com', 'info@techproservices.com'),
    (73, 'GreenTech Innovations', 'Technology', 1100000.00, 70, 'Liam Johnson', 2005, 'Denver', 'Coimbatore', 'https://www.greentechinnovations.com', 'info@greentechinnovations.com'),
    (74, 'Silver Lining Solutions', 'Consulting', 950000.00, 60, 'Ava Wilson', 2007, 'Boston', 'Bengaluru', 'https://www.silverliningsolutions.com', 'info@silverliningsolutions.com'),
    (75, 'Swift Solutions Ltd.', 'Technology', 1300000.00, 90, 'Ethan Brown', 2004, 'Manchester', 'Chennai', 'https://www.swiftsolutions.com', 'info@swiftsolutions.com'),
    (76, 'Global Tech Inc.', 'Information Technology', 1400000.00, 100, 'Mia Rodriguez', 2000, 'Houston', 'Hyderabad', 'https://www.globaltechinc.com', 'info@globaltechinc.com'),
    (77, 'Eagle Eye Consultants', 'Consulting', 900000.00, 65, 'Noah Martinez', 2012, 'Miami', 'Bengaluru', 'https://www.eagleeyeconsultants.com', 'info@eagleeyeconsultants.com'),
    (78, 'Metro Media Corporation', 'Media', 800000.00, 50, 'Harper Taylor', 2003, 'Philadelphia', 'Chennai', 'https://www.metromediacorp.com', 'info@metromediacorp.com'),
    (79, 'Ocean Blue Industries', 'Manufacturing', 1000000.00, 75, 'Logan Garcia', 1998, 'Atlanta', 'Hyderabad', 'https://www.oceanblueindustries.com', 'info@oceanblueindustries.com'),
    (80, 'InnovaTech Solutions', 'Information Technology', 1250000.00, 85, 'Avery Martin', 2006, 'Phoenix', 'Coimbatore', 'https://www.innovatechsolutions.com', 'info@innovatechsolutions.com'),
    (81, 'Bright Sparks Consulting', 'Consulting', 850000.00, 60, 'Zoe Hernandez', 2009, 'San Diego', 'Bengaluru', 'https://www.brightsparksconsulting.com', 'info@brightsparksconsulting.com'),
    (82, 'Dynamic Data Services', 'Information Technology', 1350000.00, 95, 'Carter Lewis', 2011, 'Austin', 'Chennai', 'https://www.dynamicdataservices.com', 'info@dynamicdataservices.com'),
    (83, 'Redwood Realty', 'Real Estate', 950000.00, 70, 'Ellie Thompson', 2008, 'Dallas', 'Hyderabad', 'https://www.redwoodrealty.com', 'info@redwoodrealty.com'),
    (84, 'Elite Solutions Inc.', 'Information Technology', 1300000.00, 90, 'Jackson Adams', 2005, 'San Francisco', 'Coimbatore', 'https://www.elitesolutionsinc.com', 'info@elitesolutionsinc.com'),
    (85, 'Blue Ridge Enterprises', 'Construction', 900000.00, 65, 'Addison Gray', 2010, 'Charlotte', 'Bengaluru', 'https://www.blueridgeenterprises.com', 'info@blueridgeenterprises.com'),
    (86, 'Smart Start Technologies', 'Technology', 1100000.00, 80, 'Lucy Murphy', 2003, 'Nashville', 'Chennai', 'https://www.smartstarttech.com', 'info@smartstarttech.com'),
    (87, 'Alliance Consulting Group', 'Consulting', 950000.00, 70, 'Owen Ramirez', 2007, 'Orlando', 'Hyderabad', 'https://www.allianceconsulting.com', 'info@allianceconsulting.com'),
    (88, 'Oceanic Holdings', 'Financial Services', 1150000.00, 85, 'Scarlett Scott', 2001, 'Jacksonville', 'Bengaluru', 'https://www.oceanicholdings.com', 'info@oceanicholdings.com'),
    (89, 'TechGenius Solutions', 'Information Technology', 1400000.00, 100, 'Gabriel White', 2006, 'Detroit', 'Chennai', 'https://www.techgeniussolutions.com', 'info@techgeniussolutions.com'),
    (90, 'Pinnacle Consulting', 'Consulting', 900000.00, 65, 'Isaac Flores', 2008, 'Denver', 'Hyderabad', 'https://www.pinnacleconsulting.com', 'info@pinnacleconsulting.com'),
    (91, 'Sunrise Technologies', 'Technology', 1250000.00, 90, 'Hailey Martinez', 2004, 'Portland', 'Bengaluru', 'https://www.sunrisetechnologies.com', 'info@sunrisetechnologies.com'),
    (92, 'Milestone Solutions Inc.', 'Information Technology', 1300000.00, 95, 'Christian Brown', 2012, 'Salt Lake City', 'Chennai', 'https://www.milestonesolutions.com', 'info@milestonesolutions.com'),
    (93, 'Cascade Group', 'Consulting', 850000.00, 60, 'Landon Rodriguez', 2009, 'Minneapolis', 'Hyderabad', 'https://www.cascadegroup.com', 'info@cascadegroup.com'),
    (94, 'TechNest Solutions', 'Information Technology', 1200000.00, 85, 'Aubrey Murphy', 2005, 'Oklahoma City', 'Bengaluru', 'https://www.technestsolutions.com', 'info@technestsolutions.com');
   
   SELECT * FROM Company

SELECT * FROM Company ORDER BY OfficeLocation ASC

SELECT * FROM Company WHERE OfficeLocation = 'Bengaluru' 

SELECT * FROM Company WHERE FoundedYear between 2007 and 2015 order by FoundedYear

SELECt * FROM Company WHERE Revenue between 500000 and 1000000


-- CHARATER FUNCTION 

SELECT LOWER(CompanyName) FROM Company

SELECT UPPER(CompanyName) FROM Company

SELECT * FROM Company WHERE LOWER(CompanyName)='ABC CORPORATION'

-- CHARATER MENUPULATION FUNCTION REPLACE

SELECT CompanyName,
       REPLACE(CompanyName, 'a', '') AS replaced_output
FROM Company;

--NUMRIC FUNCTION 

SELECT CAST(12.453 AS DECIMAL(38, 2)) AS RoundedNumber

SELECT FLOOR(12.90) AS ROUNDNUMBER

 -- NESTED FUNCTION

 SELECT * FROM Company ORDER BY CEOName

-- DATE FUNCTIONS 
SELECT SYSDATETIME()  AS SYSDATETIME


-- TO CHAR FUNCTION 

--SELECT FIRST_NAME, LAST_NAME,TO_CHAR(HIRE_DATE,'YYYY') FROM EMPLOYEES WHERE TO_CHAR(EMPLOYEE_ID)='100'



-- QUESTIONS  ORDER BY CLUSE 

SELECT * FROM Company ORDER BY OfficeLocation DESC

SELECT * FROM Company ORDER BY Revenue ASC



SELECT CompanyName , Industry,CEOName, OfficeLocation from Company order by OfficeLocation


SELECT * FROM Company WHERE OfficeLocation= 'BENGALURU'

SELECT * FROM  Company WHERE Revenue BETWEEN 12500 AND 10000


-- CASE EXPRESSION IN SQL 


SELECT 
    CompanyID, 
    CompanyName, 
    Industry, 
    CASE 
        WHEN Industry = 'Technology' THEN Revenue / 20
        WHEN Industry = 'Finance' THEN Revenue / 30
        WHEN Industry = 'Healthcare' THEN Revenue / 40
        ELSE 0
    END AS "Revenue"
FROM 
    Company;



SELECT 
    CompanyID,
    CompanyName,
    Industry,
    CASE
        WHEN Industry='Technology' AND EmployeeCount > 40 THEN 1
        WHEN Industry='Technology' AND EmployeeCount < 30 THEN 1
        ELSE 0
    END AS Condition
FROM 
    Company;





SELECT * FROM Company

-- VARIOUS FUNCTIONS IN SQL

SELECT AVG(Revenue) from Company 


SELECT COUNT(*) FROM Company

SELECT MAX(REVENUE) FROM Company


SELECT MAX(REVENUE) FROM Company ORDER BY CompanyName

	*/

SELECT * FROM Company

SELECT MIN(REVENUE) FROM Company

SELECT SUM(REVENUE) FROM Company

SELECT AVG(REVENUE) FROM Company WHERE Industry = 'Technology'

SELECT CompanyID, OfficeLocation, AVG(Revenue) 
FROM Company 
WHERE FoundedYear BETWEEN 1990 AND 2017 
GROUP BY CompanyID, OfficeLocation;


SELECT CompanyID, AVG(REVENUE) FROM Company GROUP BY CompanyID


-- SUB QUERY

-- SET QUERY 



SELECT EMP_ID,EMP_SALARY,EMP_DEPARTMENT FROM EMPLOYEES UNION ALL SELECT CompanyID,Revenue,HeadquartersCity FROM Company






-- DATA DEFINATION LANGUAGE 


SELECT * FROM EMPLOYEES ORDER BY EMP_SALARY


SELECT * FROM Company ORDER BY EmployeeCount

SELECT * FROM Company WHERE Industry = 'Information Technology'


SELECT * FROM Company WHERE HeadquartersCity= 'Salt Lake City'

SELECT * FROM EMPLOYEES WHERE EMP_DEPARTMENT='Engineering' ORDER BY  EMP_FIRST_NAME

SELECT * FROM Company WHERE EmployeeCount >50 

SELECT * FROM 


































































































































































































































































































































































































