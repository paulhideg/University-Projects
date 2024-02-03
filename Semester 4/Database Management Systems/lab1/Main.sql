go use BarManager

Create Table Distributors(
	DIStrid int not null,
	Name varchar(30) not null,
	Quantity int not null,
	Primary Key (DIStrid)
)

Create Table DrinkTypes(
	DTypeid int not null,
	Type varchar(30) not null,
	DIStrid int not null,
	Primary Key (DTypeid),
	FOREIGN KEY (DIStrid) REFERENCES Distributors(DIStrid)
)

INSERT INTO Distributors(DIStrid, Name, Quantity)
VALUES (1,'TheDistributor', 10), (2,'Another one',20);

INSERT INTO DrinkTypes(DTypeid, Type, DIStrid)
VALUES (3,'Exotic',2), (4,'For Kids',2);



select * from Distributors
select * from DrinkTypes

-- fpisdhjfb

Create Table UtensilsType(
	UTypeid int not null,
	Type varchar(30) not null,
	NoOfUtensils int not null,
	Primary Key (UTypeid)
)

Create Table Utensils(
	UTid int not null,
	Name varchar(30) not null,
	UTypeid int not null,
	Primary Key (UTid),
	FOREIGN KEY (UTypeid) REFERENCES UtensilsType(UTypeid)
)

DROP TABLE Utensils;

INSERT INTO UtensilsType(UTypeid, Type, NoOfUtensils)
VALUES (1,'Food', 5), (2,'Construction',20);

INSERT INTO Utensils(UTid, Name, UTypeid)
VALUES (3,'Ciocan',2), (4,'Bormasina',2);


select * from UtensilsType
select * from Utensils