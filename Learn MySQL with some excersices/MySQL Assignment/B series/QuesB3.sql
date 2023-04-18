-- B3 What is SQL Key Constraints  write an Example of SQL Key Constraints ? 

-- Constraint refers to the restriction on a column. Eg:
create table test (
	Id int not null unique,
    Name varchar(50) not null,
    Age int check(age>18)
);