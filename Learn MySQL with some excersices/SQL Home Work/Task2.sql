-- task 2:-

create database homework2;
use homework2;

create table products (
	trans_id int not null unique auto_increment,
    order_id int not null,
    product_name varchar(50) not null,
    pin_id int not null,
    quantity int not null,
	date date not null,
    primary key(trans_id),
    foreign key(pin_id) references region(pin_code) 
);

create table region(
	pin_code int not null,
    city varchar(50),
    primary key(pin_code)
);

create table Customer(
	cus_id int not null unique,
    customer_name varchar(50) not null
); 

insert into Customer(cus_id,customer_name)
values
(1,'Ritik Kohad'),
(2,'Jigar Sir'),
(3,'Kashish Patel'),
(4,'Kaveri'),
(5,'Sachnaam Singh'),
(6,'Vishal Vegada'),
(7,'Dhairya Shah'),
(8,'Keshil Soni');

insert into region (pin_code,city)
values
(380013,'Ahmedabad'),
(333509,'Surat'),
(390001,'Vadodra'),
(302001,'Jaipul'),
(110001,'Delhi'),
(530068,'Banglore'),
(560001,'Banglore'),
(560002,'Banglore');

insert into products(order_id,product_name,pin_id,quantity,date)
values
(1,'Nvidia RTX 3080','380013',5,'2021-12-08'),
(2,'AIO Cooler','333509',4,'2021-12-01'),
(3,'Corsair Ram','390001',8,'2021-11-03'),
(1,'Asus Motherboard','302001',7,'2021-12-06'),
(4,'Corsair Case','110001',9,'2021-12-26'),
(5,'logitech Mouse','530068',11,'2021-11-24'),
(5,'Logitech Keyboard','560001',2,'2021-11-13'),
(3,'LG Monitor','560002',6,'2021-1-23'),
(2,'Sony Speakers','380013',8,'2021-12-29'),
(2,'Asus Wifi Reciever','380013',1,'2021-12-06'),
(5,'Zebronics Headphones','560002',5,'2021-12-02'),
(3,'Samsung Earbuds','333509',4,'2021-10-08'),
(1,'Caps Guitar','560001',13,'2021-10-07'),
(2,'Sony Smart TV','560002',15,'2021-11-14'),
(5,'Ipad','380013',3,'2021-11-15');

select * from products
inner join region
on products.pin_id = region.pin_code
order by trans_id;

create view product_view 
as 
select products.trans_id,products.order_id,products.product_name,products.pin_id,products.quantity,products.price,products.date,region.pin_code,region.city,region.customer_name from products
inner join region
on products.pin_id = region.pin_code
order by trans_id;


-- Ques1: Find the percentage sale of banglore. 

select * from product_view;

-- formula = qty * 100 / total qty

select city,sum(quantity)as quantity, 
((select sum(quantity) from products inner join region on products.pin_id = region.pin_code where city = 'banglore') * 100/(select sum(quantity) from products))as percentage from products
inner join region 
on products.pin_id = region.pin_code
where city = 'banglore';


-- Ques 2: Find Top 3 products sold last month

select * from products 
where date between '2021-11-01' and '2021-11-30'
order by price desc;

select products.product_name,products.price,region.customer_name,products.date from products
inner join region
on products.pin_id = region.pin_code
where date between '2021-11-01' and '2021-11-30'
order by price desc
limit 3;

