-- I1  Write an SQL query that returns the departments (all fields) ordered by ascending department name.

-- tblemp(eno,ename,bdate,title,salary, dno), tblproj(pno,pname,budget,dno),   tbldept(dno,dname,mgreno), tblworkson(eno,pno,resp,hours). 

select * from dept
order by dname;