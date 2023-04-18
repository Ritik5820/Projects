-- B11 What is Difference Between DBMS and RDBMS ? 

create table DBMS_RDBMS (
	Sno int auto_increment,
    DBMS text,
    RDBMS text,
    primary key(Sno)
);

insert into dbms_rdbms (DBMS,RDBMS)
values
('DBMS applications store data as file','RDBMS applications store data in a tabular form'),
('Normalization is not present in DBMS.','Normalization is present in RDBMS.'),
('DBMS uses file system to store data, so there will be no relation between the tables.','in RDBMS, data values are stored in the form of tables, so a relationship between these data values will be stored in the form of a table as well.'),
('DBMS is meant to be for small organization and deal with small data. it supports single user.','RDBMS is designed to handle large amount of data. it supports multiple users.'),
('Examples of DBMS are file systems, xml etc.','Example of RDBMS are mysql, postgre, sql server, oracle etc.');

select * from dbms_rdbms;