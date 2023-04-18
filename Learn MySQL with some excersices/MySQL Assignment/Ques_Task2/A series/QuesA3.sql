-- A3  Write an SQL query that returns the employee name, project name, employee title and hours for all works on records. 

-- tblemp(eno,ename,bdate,title,salary, dno), tblproj(pno,pname,budget,dno),   tbldept(dno,dname,mgreno), tblworkson(eno,pno,resp,hours). 


select ename,pname,title,hours from empl
inner join proj 
on emp.dno = proj.dno
inner join workson
on emp.eno = workson.eno;
