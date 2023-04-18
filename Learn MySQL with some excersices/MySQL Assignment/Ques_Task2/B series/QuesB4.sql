-- B4 Write an SQL query that returns the employees (name only) in department “D1‟ordered by decreasing salary. 

-- tblemp(eno,ename,bdate,title,salary, dno), tblproj(pno,pname,budget,dno),   tbldept(dno,dname,mgreno), tblworkson(eno,pno,resp,hours). 

select ename from emp 
inner join dept
on emp.dno = dept.dno
where dname = "D1"
order by salary desc;