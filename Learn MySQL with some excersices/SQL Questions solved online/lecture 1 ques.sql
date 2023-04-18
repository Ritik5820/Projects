-- lecture 1 online Questions

create database lecture1;
create table album (
	aid int,
    name varchar(50),
    selling_price int,
    copies_sold int,
    sid int,
    foreign key(sid) references sales_person(sid)
);


create table Sales_person(
	sid int, 
    name varchar(50),
    region varchar(10),
    primary key(sid)
);


insert into sales_person(sid,name,region)
values
(1,'Ritik Kohad','East'),
(2,'Kashish Patel','West'),
(3,'Jigar sir','North'),
(4,'Dhairya Shah','South'),
(5,'Sachnaam Singh','East'),
(6,'Venu Gopal Ayer','West');

insert into album(aid,name,selling_price,copies_sold,sid)
values
(1,'Arijit Singh',200,10000,1),
(2,'Jubin Nautiyal',300,110000,2),
(3,'Ayushmaan Khurana',250,9000,1),
(4,'Rihana',500,50000,3),
(5,'Beyonce',900,80000,4),
(6,'Justin',200,2000,5),
(7,'Unknown album',100,1090,5),
(8,'123',200,10020,6);

select album.aid,album.name,album.selling_price,album.copies_sold,sales_person.name,sales_person.region from album
inner join sales_person
on album.sid = sales_person.sid;

-- Ques1 which region's salesperson has the highest sold copies.

select sales_person.name,max(copies_sold) from album
inner join sales_person
on album.sid = sales_person.sid
where sales_person.region = 'east'
;

-- Ques2 Which region has sold the highest album
select sales_person.region from album
inner join sales_person
on album.sid = sales_person.sid
where album.copies_sold = (select max(album.copies_sold) from album);

-- Ques3 Which album has avg copies sold?
select album.name,avg(album.copies_sold) from album
inner join sales_person
on album.sid = sales_person.sid;

-- Ques4 which sales person has sold max copies on an avg
select sales_person.name , avg(album.copies_sold) from album
inner join sales_person
on album.sid = sales_person.sid
group by album.sid;


select sales_person.name , avg(album.copies_sold) as average from album
inner join sales_person
on album.sid = sales_person.sid
group by album.sid
order by average desc
limit 1;

