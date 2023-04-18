create database homework;
use homework;

create table product (
	pid int,
    product_name varchar(50),
    product_price int,
    primary key(pid)
);

insert into product (pid,product_name,product_price)
values
(1,'Patanjali Dant Kanti',2500),
(2,'Balaji Wafers',2000),
(3,'Nvidia RTX 3080',150000),
(4,'Intel i9 10850k',36000),
(5,'TUF Gaming Z590',22000);

create table department(
	did int,
    dept_name varchar(50),
    primary key(did)
);

insert into department(did,dept_name)
values
(1,'Sales Department'),
(2,'Finance Department'),
(3,'R&D'),
(4,'Purchase Department'),
(5,'HR Department');

create table salary (
	exp_id int,
    exp varchar(50),
    salary int,
    primary key(exp_id)
);


create table employee(
	id int,
    name varchar(50),
    product int,
    department int,
    emp_level int,
    salary int,
    foreign key(product) references product(pid),
    foreign key(department) references department(did)
);

insert into employee(id,name,product,department,emp_level,salary)
values
(1,'Ritik Kohad',4,5,7,100000),
(2,'Kartik Kohad',3,4,1,115000),
(3,'Devika Kohad',5,1,8,120000),
(4,'Kailash Kohad',5,5,10,200000),
(5,'Kashish patel',4,2,8,107000),
(6,'Jigar Parmar sir',5,2,10,199500),
(7,'Sachnaam Singh',2,4,5,80000),
(8,'Dhairya Shah',3,3,1,15000),
(9,'Vishal Vegada',3,2,3,21000),
(10,'Keshil Soni',4,1,2,18000),
(11,'Adiya Jha',1,1,4,25000),
(12,'Shreya Rathod',1,2,6,85000),
(13,'Mansi Patel',5,4,7,103000),
(14,'Deep Mehta',4,5,8,121000),
(15,'Mangal Pandey',1,1,9,191250);

select e.id,e.name,e.emp_level,e.salary,p.product_name,p.product_price,d.dept_name from employee e
inner join product p
on e.product = p.pid
inner join department d 
on e.department = d.did
order by id;
commit;

-- Ques1: Find out the highest salary in each dept. 


select department.dept_name,max(employee.salary) as Maximum_salary from employee
inner join product
on employee.product = product.pid
inner join department 
on employee.department = department.did
group by department.dept_name;

-- Ques2: Find out the most expensive product. 

select employee.name,product.product_name,product.product_price from employee
inner join product
on employee.product = product.pid
inner join department 
on employee.department = department.did
where product.product_price = (select max(product.product_price) from product);



















