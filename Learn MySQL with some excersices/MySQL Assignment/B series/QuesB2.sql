-- B2 How to Create a Exam table with Foreign key on rollno write a SQL Query  ? 

create table Exam (
	Roll_no int not null unique,
    S_code varchar(50) not null,
    Marks int not null,
    P_code varchar(50),
    foreign key(Roll_no) references Student(Roll_no)
);