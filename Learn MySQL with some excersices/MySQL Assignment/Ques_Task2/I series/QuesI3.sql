-- I3  Write SQL query that returns the project name, hours worked, and project number for all works on records where hours > 10. 

-- tblemp(eno,ename,bdate,title,salary, dno), tblproj(pno,pname,budget,dno),   tbldept(dno,dname,mgreno), tblworkson(eno,pno,resp,hours). 

select pname,hours,pno from proj
inner join workson 
on proj.pno = workson.pno
where hours > 10;