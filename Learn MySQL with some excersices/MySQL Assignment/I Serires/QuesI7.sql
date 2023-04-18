-- Get department wise maximum salary from employee table order by salary ascending. 

select Department,max(salary)as Total_salary from employee
group by department
order by Total_salary;