-- B3 Return the FirstName,LastName,SalePrice,RecommendedSalePrice, and the difference between the SalePrice and Recommended SalePrice for all Sales. The difference 
-- must  be returned  as  a  positive number

select * from sales 
inner join products
on sales.pid = products.Pid
inner join customers
on sales.Cid = customers.Cid
order by sales.Sid;

select customers.First_name,customers.Last_name,sales.Sales_price,products.Recommended_price,
(select abs(sales.Sales_price - products.Recommended_price))as difference from sales 
inner join products
on sales.pid = products.Pid
inner join customers
on sales.Cid = customers.Cid;