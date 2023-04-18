-- B4 What is SQL View Create a View of Student Table  ? 
-- View is nothing but a stored commands or query. Its useful when we are working on multiple tables and if we want to see the contents of the table then we would 
-- have to write the whole syntax again and again. So instead of writing whole syntax again, we store that query in a veiw. 


create view Student_view as
select * from student ;
