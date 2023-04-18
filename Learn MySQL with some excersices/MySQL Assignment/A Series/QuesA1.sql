SET FOREIGN_KEY_CHECKS=0;
create table Sales_person (
	Sno int primary key,
    Sname varchar(50),
    city varchar(50),
    Comm int
);

create table Customer (
	Cnm int primary key,
    Cname varchar(50),
    city varchar(50),
    Rating int,
    Sno int,
    foreign key(Sno) references sales_person(Sno)
);

create table orrder (
	Onm int primary key,
    Amt Float,
    Ode date,
    Cnm int,
    Sno int,
    foreign key(Cnm) references customer(Cnm),
    foreign key(Sno) references customer(Sno)
);

insert into sales_person(Sno,Sname,city,Comm)
values
(1001,'Peel','London',0.12),
(1002,'Serres','San Jose',0.13),
(1004,'Motika','London',0.11),
(1007,'Rafkin','Barcelona',0.15),
(1003,'Axelrod','New York',0.1);

insert into customer(Cnm,Cname,city,Rating,Sno)
values
(201,'Hoffman','London',100,1001),
(202,'Giovanne','Roe',200,1003),
(203,'Liu','San Jose',300,1002),
(204,'Grass','Barcelona',100,1002),
(206,'Clemens','London',300,1007),
(207,'Pereira','Roe',100,1004);

insert into orrder (Onm,Amt,Ode,Cnm,Sno)
values
(3001,18.69,'1994-10-03',2008,1007),
(3003,767.19,'1994-10-03',2001,1001),
(3002,1900.10,'1994-10-03',2007,1004),
(3005,3005,'1994-10-03',2003,1002),
(3006,3006,'1994-10-04',2008,1007),
(3009,3009,'1994-10-04',2002,1003),
(3007,3007,'1994-10-05',2004,1002),
(3008,3008,'1994-10-05',2006,1001),
(3010,3010,'1994-10-06',2004,1002),
(3011,3011,'1994-10-06',2006,1001);

-- A1 All orders for more than $1000. 

select * from orrder
where Amt > 1000;