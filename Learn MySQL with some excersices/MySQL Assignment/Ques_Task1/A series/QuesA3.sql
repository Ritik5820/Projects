-- A3 Largest order taken by each salesperson, datewise. 

select customers.First_name, max(sales.Sales_price)as largest_order, sales.Sales_date from sales
inner join customers
on sales.Cid = customers.Cid
group by customers.First_name;  