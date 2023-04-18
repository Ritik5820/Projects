-- Update the Sale Price to the Recommended Sale Price of those Sales occurring between 6/10/2005and6/20/2005. 

select sales.sid,sales.Sales_price,products.Recommended_price,sales.Sales_date,sales.updated_salesPrice from sales
inner join products
on sales.Pid = products.pid
where sales.Sales_date between "2005-06-10" and "2005-06-20"
order by sales.sid;

update sales 
set updated_salesPrice = (case sales.sid
	when 1 then 130 -- change to 105
    when 2 then 97 -- change to 98
    when 28 then 285 -- change to 200
end)
where sales.sid in (1,2,28);
