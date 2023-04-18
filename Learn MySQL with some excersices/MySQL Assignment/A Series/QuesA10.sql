-- A10 All customers excluding those with rating <= 100 unless they are located in Rome. 

select * from customer
where rating > 100 or (city = "rome" and rating <=100);