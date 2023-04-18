-- B2 Write an SQL query that returns all works on records where hours worked is less than10and the responsibility is “Manager”. 
-- tblemp(eno,ename,bdate,title,salary, dno), tblproj(pno,pname,budget,dno),   tbldept(dno,dname,mgreno), tblworkson(eno,pno,resp,hours). 

select * from workson
where hours<10 and resp = "Manager";