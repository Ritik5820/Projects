-- I8  Select first_name, incentive amount from employee and incentives table for those employees who have incentives and incentive amount greater than 3000 

select First_name,Incentive_amount from employee
inner join incentive
on employee.Employee_id = incentive.Employee_ref_id
where incentive.Incentive_amount > 3000;