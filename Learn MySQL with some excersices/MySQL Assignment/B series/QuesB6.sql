-- B6 What is SQL and How to Create a table with Forign Key  ? 

-- SQL stands for structured query language which is used to access and manipulate databases. 
create table Exam (
	Roll_no int not null unique,
    S_code varchar(50) not null,
    Marks int not null,
    P_code varchar(50),
    foreign key(Roll_no) references Student(Roll_no)
);