create table products (
	Pid int primary key auto_increment,
    Product_name varchar(50),
    Recommended_price int,
    Category varchar(10) 
);

create table customers (
	Cid int primary key auto_increment,
	First_name varchar(50),
    Last_name varchar(50),
    City varchar(50),
    State char(2),
    Zip varchar(10)
);

create table Sales (
	Sid int primary key auto_increment,
    Pid int,
    Cid int,
    Sales_price int , 
    Sales_date datetime,
    foreign key(pid) references products(pid),
    foreign key(cid) references customers(Cid)
);

insert into products(product_name,recommended_price,category)
values
("DVD",105,"LivingRoom"),
("Microwave",98,"Kitchen"),
("Monitor",200,"Office"),
("Speaker",85,"Office"),
("Refrigerator",900,"Kitchen"),
("VCR",165,"LivingRoom"),
("CoffeePot",35,"Kitchen");

insert into customers(First_name,Last_name,City,State,Zip)
values
("Chintan","Patel","Anand","GJ","388001"),
("Paresh","Prajapati","Nadiad","GJ","387001"),
("Pragnesh","Patel","Surat","GJ","395008"),
("Nilesh","Dharsandia","Mumbai","MH","400002"),
("Sonal","Patel","Mumbai","MH","400002"),
("Harshal","Patel","Mogri","GJ","388345"),
("Prakash","Rathod","Mogri","GJ","388345"),
("Aarzoo","Dodhiya","Rajkot","GJ","360003"),
("Heta","Dave","Varanasi","UP","221002"),
("Nikita","Dave","Varanasi","UP","221002"),
("Vaibhav","Dave","Varanasi","UP","221002"),
("Paresh","Patel","Pune","MH","411001"),
("Prakash","Patel","Pune","MH","411001"),
("Sandhya","Patel","Hydrabad","Ap","500031"),
("Divesh","Patel","Banglore","KA","560002"),
("Payal","Shah","Banglore","KA","560002"),
("Priyanka","Rana","Anand","GJ","388001"),
("Sanket","Dhebar","V.V.nagar","GJ","388121"),
("Puja","Shah","Varanasi","UP","221002"),
("Priya","Shah","Varanasi","UP","221002");

insert into sales(Pid,Cid,Sales_price,Sales_date)
values
(1,1,130,"2005-06-14"),
(2,2,97,"2005-06-19"),
(3,3,200,"2005-09-20"),
(4,4,80,"2005-03-22"),
(5,5,899,"2005-01-23"),
(6,6,150,"2005-03-24"),
(3,7,209,"2005-03-10"),
(4,8,90,"2005-08-11"),
(6,9,130,"2005-08-12"),
(2,14,85,"2005-12-13"),
(3,15,240,"2005-05-14"),
(1,17,87,"2005-07-19"),
(2,18,99,"2005-09-20"),
(6,19,150,"2005-07-22"),
(5,5,900,"2005-03-06"),
(4,6,86,"2005-04-07"),
(2,7,88,"2005-11-08"),
(3,8,198,"2005-05-09"),
(1,9,150,"2005-10-10"),
(6,14,99,"2005-05-09"),
(6,15,104,"2005-09-20"),
(4,14,90,"2005-07-22"),
(1,1,130,"2005-03-06"),
(2,2,102,"2005-04-07"),
(1,3,114,"2005-11-08"),
(5,4,1000,"2005-05-09"),
(5,5,1100,"2005-10-10"),
(3,6,285,"2005-06-11"),
(2,7,87,"2005-10-12"),
(3,8,300,"2005-07-13"),
(3,20,205,"2005-12-31");

-- B1 FirstName,  LastName,  ProductName,  and  SalePrice  for all products  sold  in  the  month  of October200
-- reference table: 
select * from sales 
inner join products
on sales.pid = products.Pid
inner join customers
on sales.Cid = customers.Cid
order by sales.Sid;

select customers.First_name,customers.Last_name,products.Product_name,sales.Sales_price,sales.Sales_date from sales 
inner join products
on sales.pid = products.Pid
inner join customers
on sales.Cid = customers.Cid
where sales.Sales_date between "2005-10-01" and "2005-10-31";
