-- B3 Write an SQL query that returns the employees (number and name only) who have a title of “EEE‟ or “SA‟ and make more than $35,000. 
-- tblemp(eno,ename,bdate,title,salary, dno), tblproj(pno,pname,budget,dno),   tbldept(dno,dname,mgreno), tblworkson(eno,pno,resp,hours). 

select eno,ename from emp 
where title in ("EEE","SA") and salary > 35000;