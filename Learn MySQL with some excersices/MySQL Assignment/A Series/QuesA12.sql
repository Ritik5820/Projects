-- A12 Count the number of salespeople currently listing orders in the order table. 

-- showing full table for reference: 
select * from sales_person s 
inner join orrder o
on s.Sno = o.Sno;

select count(distinct(Sname)) from sales_person s 
inner join orrder o
on s.Sno = o.Sno;