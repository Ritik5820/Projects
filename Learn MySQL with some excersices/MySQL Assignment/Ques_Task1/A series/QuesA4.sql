--  A4 Without using a declared iterative construct, return Sale Date and the running total for all sales, ordered by the Sale Date in Ascending Order. 

select sales.Sales_date, sales.Sales_price from sales
group by sales.Sales_date
order by sales.Sales_date;