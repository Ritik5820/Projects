-- A13 Largest order taken by each salesperson, datewise. 

-- reference table below: 
select * from sales_person s 
inner join orrder o
on s.Sno = o.Sno;

select sales_person.Sname,max(orrder.Amt)as Largest_Order,orrder.Ode from sales_person
inner join orrder
on sales_person.Sno = orrder.Sno
group by sales_person.Sname
order by ode;