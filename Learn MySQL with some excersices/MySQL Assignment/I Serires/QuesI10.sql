-- I10 Select first_name, incentive amount from employee and incentives table for    all employees who got incentives using left join. 

select First_name,Incentive_amount from employee
left join incentive
on employee.Employee_id = incentive.Employee_ref_id;