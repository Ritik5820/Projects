-- A1  Write an SQL query that returns the project name, department name, and budget for all projects with a budget < $50,000. 

-- tblemp(eno,ename,bdate,title,salary, dno), tblproj(pno,pname,budget,dno),   tbldept(dno,dname,mgreno), tblworkson(eno,pno,resp,hours). 

select pname,dname,budget from proj
inner join dept
on proj.dno = dept.dno 
where budget < 50000;