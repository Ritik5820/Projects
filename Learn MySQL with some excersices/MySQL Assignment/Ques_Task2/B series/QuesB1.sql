-- B1  Write an SQL query that returns the project number and name for projects with a budget greater than $100,000.                
-- tblemp(eno,ename,bdate,title,salary, dno), tblproj(pno,pname,budget,dno),   tbldept(dno,dname,mgreno), tblworkson(eno,pno,resp,hours). 


select * from pno,pname from proj
where budget > 100000;