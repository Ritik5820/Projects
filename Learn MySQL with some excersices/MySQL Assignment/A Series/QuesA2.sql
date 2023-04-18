-- A2 Names and cities of all salespeople in London with commission above 0.10.

select Sname,city from sales_person
where city = "London" and comm > 0.10;