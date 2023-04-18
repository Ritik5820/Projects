-- Get department, total salary with respect to a department from employee table order by total salary descending. 

select Department, sum(salary)as Total_salary from employee
group by department
order by Total_salary desc;