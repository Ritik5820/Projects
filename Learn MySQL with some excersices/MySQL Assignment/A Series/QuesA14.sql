-- A14  Largest order taken by each salesperson with order value more than $3000.

-- reference table
select * from sales_person s 
inner join orrder o
on s.Sno = o.Sno;

select sales_person.Sname,max(orrder.Amt) as Largest_order from sales_person
inner join orrder
on sales_person.Sno = orrder.Sno
group by sales_person.Sname
having Largest_order > 3000;