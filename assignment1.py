CREATE DATABASE sales_and_custmores; 
use sales_and_custmores;

create table salespeople (
snum int primary key,
sname varchar(20) unique,
city varchar(20),
comm int
);

insert into salespeople (snum,sname,city,comm) values (1001,"peel","london",12);
insert into salespeople (snum,sname,city,comm) values (1002,"serrs","sanjose",13);
insert into salespeople (snum,sname,city,comm) values (1004,"motika","london",11);
insert into salespeople (snum,sname,city,comm) values (1007,"rifkin","barcelone",15);
insert into salespeople (snum,sname,city,comm) values (1003,"axelord","newyoke",10);
select * from salespeople;

create table custmores(
cnum int primary key,
cname varchar(20),
city varchar(20) not null,
snum int,
foreign key (snum)
references salespeople (snum)
);

insert into custmores(cnum,cname,city,snum) values(2001,"hoffman","london",1001);
insert into custmores(cnum,cname,city,snum) values(2002,"giovanni","romo",1003);
insert into custmores(cnum,cname,city,snum) values(2002,"liu","sanjose",1002);
insert into custmores(cnum,cname,city,snum) values(2004,"grass","berlin",1002);
insert into custmores(cnum,cname,city,snum) values(2006,"clemens","london",1001);
insert into custmores(cnum,cname,city,snum) values(2008,"cisencros","sanjose",1007);
insert into custmores(cnum,cname,city,snum) values(2007,"pereira","rome",1004);

select * from custmores;


create table orders(
onum int primary key,
amt float,
odate varchar(50),
cnum int,
snum int,
foreign key(cnum)
references custmores(cnum),
foreign key(snum)
references salepeople(snum)
);
insert into orders(onum,amt,odate,cnum,snum) values(3001,18.69,"3-10-1990",2008,1007);
insert into orders(onum,amt,odate,cnum,snum) values(3003,767.19,"3-10-1990",2001,1001);
insert into orders(onum,amt,odate,cnum,snum) values(3002,1900.10,"3-10-1990",2007,1004);
insert into orders(onum,amt,odate,cnum,snum) values(3005,5160.45,"3-10-1990",2003,1002);
insert into orders(onum,amt,odate,cnum,snum) values(3006,1098.16,"3-10-1990",2008,1007);
insert into orders(onum,amt,odate,cnum,snum) values(3009,1713.23,"4-10-1990",2002,1003);
insert into orders(onum,amt,odate,cnum,snum) values(3007,75.75,"4-10-1990",2004,1002);
insert into orders(onum,amt,odate,cnum,snum) values(3008,4273.00,"5-10-1990",2006,1001);
insert into orders(onum,amt,odate,cnum,snum) values(3010,1309.95,"6-10-1990",2004,1002);
insert into orders(onum,amt,odate,cnum,snum) values(3011,9891.88,"6-10-1990",2006,1001);

select * from orders;


# Q1
select 
  count(*)
from
  salespeople
where
  sname like '%A' or '%a' ;
  
#Q2
select snum,onum,amt from orders where amt > 2000;
# or for full into
select * from orders where amt > 2000;

#Q3
Select
  sname,city,count(*)
from
  salespeople
where
  city='newyork'
group by sname,city;

#Q4
select
 sname,city,count(*)
from
 salespeople
where
 city='london' or city='paris'
group by sname,city;

#Q5
select 
 odate,snum,count(*)
from
 orders
group by odate,snum;
