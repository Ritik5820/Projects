-- I11  Create View OF Employee table in which store first name ,last name and salary only. 

create view Employee_view 
as 
select first_name,last_name,salary from employee;

select * from employee_view;