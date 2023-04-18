-- I1 Get First_Name from employee table using alias name “Employee Name”. 

create table employee(
	Employee_id int,
    First_name varchar(50),
    Last_name varchar(50),
    Salary int,
    Joining_date datetime,
    Department varchar(50)
);

create table incentive(
	Employee_ref_id int,
    Incentive_date date,
    Incentive_amount int
);

insert into employee(Employee_id,First_name,Last_name,Salary,Joining_date,Department)
values

(2,'Michael','Clark',800000,'2013-01-01 00.00.00','Insurance'),
(3,'Roy','Thomas',700000,'2013-02-01 00.00.00','Banking'),
(4,'Tom','Jose',600000,'2013-02-01 00.00.00','Insurance'),
(5,'Jerry','Pinto',650000,'2013-02-01 00.00.00','Insurance'),
(6,'Philip','Mathew',750000,'2013-01-01 00.00.00','Services'),
(7,'TestName1','123',650000,'2013-01-01 00.00.00','Services'),
(8,'TestName2','Lname%',600000,'2013-02-01 00.00.00','Insurance');

insert into incentive(Employee_ref_id,Incentive_date,Incentive_amount)
values
(1,'2013-02-01',5000),
(2,'2013-02-01',3000),
(3,'2013-02-01',4000),
(1,'2013-01-01',4500),
(2,'2013-01-01',3500);

-- I1 Get First_Name from employee table using alias name “Employee Name”. 

select First_name as Employee_name from employee;
