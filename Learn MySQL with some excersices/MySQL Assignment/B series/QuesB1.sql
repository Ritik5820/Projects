create database Assignment;
use assignment;

-- B1 How to Create an Table student write an SQL Query ? 

create table student (
	Roll_no int not null unique primary key,
    Name varchar(50),
    Branch_name varchar(50)
);