-- A8 All salespeople either in Barcelona or in London. 

select * from sales_person
where city = "Barcelona" or city = "London";