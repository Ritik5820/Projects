-- I2  Write an SQL query that returns the employee name, department name, and employee title.

-- tblemp(eno,ename,bdate,title,salary, dno), tblproj(pno,pname,budget,dno),   tbldept(dno,dname,mgreno), tblworkson(eno,pno,resp,hours). 

select ename,dname,title from emp
inner join dept
on emp.dno = dept.dno;