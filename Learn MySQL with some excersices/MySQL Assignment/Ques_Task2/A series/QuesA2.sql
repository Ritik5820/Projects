-- A2  Write an SQL query that returns the employee numbers and salaries of all employees in the “Consulting” department ordered by descending salary. 

-- tblemp(eno,ename,bdate,title,salary, dno), tblproj(pno,pname,budget,dno),   tbldept(dno,dname,mgreno), tblworkson(eno,pno,resp,hours). 

select eno,salary from emp
inner join dept
on emp.dno = dept.dno
where dname = "Consulting" 
order by salary desc;