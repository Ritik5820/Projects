-- What is store Proceedure write a query of creating store Proceedure  ? 

-- Its similar in some ways to view. A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

delimiter //
create procedure student_pro()
begin
	select * from student;
end//


call student_pro()