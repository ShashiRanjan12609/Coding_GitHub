create table Emps ( 
emp_no int not null,
birth_date date not null,
firstname varchar(20) not null,
lastname varchar (15) not null,
gender varchar(7) not null,
hire_date date not null,
primary key (emp_no));

INSERT INTO Emps (emp_no, birth_date, firstname, lastname, gender, hire_date)
VALUES
(1, '1990-05-01', 'Rahul', 'Sharma', 'Male', '2010-01-15'),
(2, '1988-07-12', 'Priya', 'Patel', 'Female', '2012-03-20'),
(3, '1992-09-25', 'Amit', 'Singh', 'Male', '2015-06-10'),
(4, '1995-03-18', 'Anjali', 'Yadav', 'Female', '2018-02-28'),
(5, '1993-11-30', 'Vivek', 'Gupta', 'Male', '2016-09-05'),
(6, '1991-08-22', 'Pooja', 'Joshi', 'Female', '2013-07-15'),
(7, '1989-06-05', 'Neha', 'Shah', 'Female', '2011-11-20'),
(8, '1994-02-14', 'Sachin', 'Verma', 'Male', '2017-04-12'),
(9, '1996-12-08', 'Kavita', 'Kumar', 'Female', '2019-08-10'),
(10, '1997-04-25', 'Raj', 'Sinha', 'Male', '2020-01-02'),
(11, '1987-10-10', 'Manoj', 'Sharma', 'Male', '2009-12-15'),
(12, '1990-01-05', 'Shweta', 'Gandhi', 'Female', '2010-07-20'),
(13, '1993-06-17', 'Sandeep', 'Mishra', 'Male', '2016-03-25'),
(14, '1988-03-22', 'Deepika', 'Reddy', 'Female', '2012-09-18'),
(15, '1991-09-14', 'Vikram', 'Nair', 'Male', '2014-05-30'),
(16, '1995-07-28', 'Ananya', 'Menon', 'Female', '2018-11-08'),
(17, '1994-04-02', 'Rajesh', 'Iyer', 'Male', '2017-08-15'),
(18, '1989-12-20', 'Meera', 'Pillai', 'Female', '2011-04-05'),
(19, '1992-11-09', 'Amitabh', 'Rao', 'Male', '2015-01-20'),
(20, '1996-08-03', 'Anita', 'Chopra', 'Female', '2019-02-10'),
(21, '1986-02-18', 'Kunal', 'Malhotra', 'Male', '2008-06-22'),
(22, '1990-10-28', 'Ritu', 'Srivastava', 'Female', '2010-12-05'),
(23, '1993-05-15', 'Akash', 'Ganguly', 'Male', '2016-01-08'),
(24, '1997-01-20', 'Aarti', 'Roy', 'Female', '2020-07-12'),
(25, '1994-08-12', 'Rohit', 'Chatterjee', 'Male', '2018-03-15'),
(26, '1988-06-23', 'Shikha', 'Mukherjee', 'Female', '2012-10-30'),
(27, '1991-03-07', 'Saurabh', 'Banerjee', 'Male', '2013-11-22'),
(28, '1995-09-29', 'Divya', 'Sharma', 'Female', '2017-05-18'),
(29, '1992-12-03', 'Amita', 'Das', 'Female', '2015-02-25'),
(30, '1987-07-16', 'Anand', 'Narayan', 'Male', '2009-09-20');

Select * from Emps where gender = 'Male';