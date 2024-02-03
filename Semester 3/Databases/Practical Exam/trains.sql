-------PART I------------------------

--drop table R
create table R(
    FK1 int not null,
    FK2 int not null,
    C1 varchar(100) not null,
    C2 varchar(50) not null,
    C3 int,
    C4 int,
    C5 varchar(20),
    CONSTRAINT pk_R PRIMARY KEY(FK1, FK2))
    
insert into R(FK1, FK2, C1, C2, C3, C4, C5) values 
(1, 1, 'Pisica pe acoperisul fierbinte', 'Tennessee Williams', 100, 20, 'AB'),
(1, 2, 'Conul Leonida fata cu reactiunea', 'Ion Luca Caragiale', 50, 50, 'CQ'),
(1, 3, 'Concert din muzica de Bach', 'Hortensia Papadat-Bengescu', 50, 10, 'QC'),
(2, 1, 'Fata babei si fata mosneagului', 'Ion Creanga', 100, 100, 'QM'),
(2, 2, 'Frumosii nebuni ai marilor orase', 'Fanus Neagu', 10, 10, 'BA'),
(2,  3,  'Frumoasa  calatorie ',  'Matei Visniec', 100, 20, 'MQ'),
(3, 1, 'Mansarda la Paris cu vedere spre moarte', 'Matei Visniec', 200, 10, 'PQ'),
(3, 2, 'Richard al III-lea se int', 'Matei Visniec', 100, 50, 'PQ'),
(3, 3, 'Masinaria Cehov. Nina s', 'Matei Visniec', 100, 100, 'AZ'),
(4, 1, 'Omul de zapada care voia sa intalneasca soarele', 'Matei Visniec', 100,100, 'CP'),
(4, 2, 'Extraterestrul care isi dorea ca amintire o pijama', 'Matei Visniec', 50, 10, 'CQ'),
(4, 3, 'O femeie draguta cu o floare si ferestre spre nord', 'Edvard Radzinski', 10, 100, 'CP'),
(4, 4, 'Trenul din zori nu mai opreste aici', 'Tennessee Williams', 200, 200, 'MA')

--Queries

--1. Consider query Q below:
SELECT C2, SUM(C3) TotalC3, AVG(C3) AvgC3 
FROM R
WHERE C3 >= 100 OR C1 LIKE '%Pisica%'
GROUP BY C2
HAVING SUM(C3) > 100


--2. How many records does the following query return? 
SELECT * 
FROM 
(SELECT FK1, FK2, C3+C4 TotalC3C4 FROM R
WHERE FK1 = FK2) r1 
INNER JOIN (SELECT FK1, FK2, C5 
FROM R 
WHERE C5 LIKE '%Q%') r2 ON r1.FK1 = r2.FK1 AND r1.FK2 = r2.FK2 

--3
/*
CREATE OR ALTER TRIGGER TrOnUpdate 
ON R 
FOR UPDATE AS 
DECLARE @total INT = 0
SELECT @total = SUM(i.C3 -d.C3)
FROM deleted d INNER JOIN inserted i ON d.FK1 = i.FK1 AND d.FK2 = i.FK2 WHERE d.C3 < i.C3
PRINT @total */

UPDATE R
SET C3 = 300
WHERE FK1 < FK2 


--4




--------PART II----------------------------

/*
Create a database to manage a chocolate shop. The database will store data about the presents that contain chocolate.
The entities of interest to the problem domain are: Chocolate Type, Chocolate, Present and Child. 
Each chocolate has a name, a weight, a price and belongs to a type. A chocolate type has besides the name, also a description.
Each present has a title, a description, a price and a list of chocolates with the quantity and the expiration date included.
A child has a name, surname, age, gender and a list of chocolates with the reccomended quantity to be eaten.
1) Write an SQL script that creates the corresponding relational data model.
2) Implement a stored procedure that receives a chocolate, a present, a quantity an expiration date and adds the chocolate to the present.
If the chocolate is already included in the present, the quantity and the expiration date are updated. 
3) Create a view that shows the names of the chocolates included in all the presents. 
4) Implement a function that lists the names of the children that haven't received any chocolate.
*/


