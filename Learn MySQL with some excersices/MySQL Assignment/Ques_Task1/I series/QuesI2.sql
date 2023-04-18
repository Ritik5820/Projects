-- Return the Product Category and the average Sale Price for those customers who have purchased two or more products. 

select * from sales 
inner join products
on sales.pid = products.Pid
inner join customers
on sales.Cid = customers.Cid
order by sales.Sid;


select customers.cid,customers.First_name,count(products.Pid)as Total_purchase, products.Category,sales.Sales_price,avg(sales.Sales_price) from sales 
inner join products
on sales.pid = products.Pid
inner join customers
on sales.Cid = customers.Cid
group by customers.cid
having Total_purchase > 1
order by customers.cid;