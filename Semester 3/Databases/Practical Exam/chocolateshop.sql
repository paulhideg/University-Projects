/*Create a database to manage a chocolate shop. The database will store data about the presents that contain chocolate.
The entities of interest to the problem domain are: Chocolate Type, Chocolate, Present and Child. Each chocolate has a name, a weight, a price and belongs to a type. A chocolate type has besides the name, also a description.Each present has a title, a description, a price and a list of chocolates with the quantity and the expiration date included.
A child has a name, surname, age, gender and a list of chocolates with the reccomended quantity to be eaten.*/

-- 1) Write an SQL script that creates the corresponding relational data model.

CREATE TABLE ChocolateType(
    ChocolateTypeId INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Description VARCHAR(100) NOT NULL
);
CREATE TABLE Chocolate(
    ChocolateId INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Weight INT NOT NULL,
    Price INT NOT NULL,
    ChocolateTypeId INT NOT NULL,
    CONSTRAINT FK_Chocolate_ChocolateType FOREIGN KEY (ChocolateTypeId) REFERENCES ChocolateType(ChocolateTypeId)
);
CREATE TABLE Present(
    PresentId INT IDENTITY(1,1) PRIMARY KEY,
    Title VARCHAR(50) NOT NULL,
    Description VARCHAR(100) NOT NULL,
    Price INT NOT NULL
);
CREATE TABLE Child(
    ChildId INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Surname VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Gender VARCHAR(1) NOT NULL
);
CREATE TABLE ChocolatePresent(
    ChocolatePresentId INT IDENTITY(1,1) PRIMARY KEY,
    ChocolateId INT NOT NULL,
    PresentId INT NOT NULL,
    Quantity INT NOT NULL,
    ExpirationDate DATE NOT NULL,
    CONSTRAINT FK_ChocolatePresent_Chocolate FOREIGN KEY (ChocolateId) REFERENCES Chocolate(ChocolateId),
    CONSTRAINT FK_ChocolatePresent_Present FOREIGN KEY (PresentId) REFERENCES Present(PresentId)
);
CREATE TABLE ChocolateChild(
    ChocolateChildId INT IDENTITY(1,1) PRIMARY KEY,
    ChocolateId INT NOT NULL,
    ChildId INT NOT NULL,
    Quantity INT NOT NULL,
    CONSTRAINT FK_ChocolateChild_Chocolate FOREIGN KEY (ChocolateId) REFERENCES Chocolate(ChocolateId),
    CONSTRAINT FK_ChocolateChild_Child FOREIGN KEY (ChildId) REFERENCES Child(ChildId)
);
-- Add some data to the tables
INSERT INTO ChocolateType(Name, Description) VALUES('Dark', 'Dark chocolate')
INSERT INTO ChocolateType(Name, Description) VALUES('Milk', 'Milk chocolate')
INSERT INTO ChocolateType(Name, Description) VALUES('White', 'White chocolate')

INSERT INTO Chocolate(Name, Weight, Price, ChocolateTypeId) VALUES('Milka', 100, 10, 1)
INSERT INTO Chocolate(Name, Weight, Price, ChocolateTypeId) VALUES('Primola', 100, 15, 2)
INSERT INTO Chocolate(Name, Weight, Price, ChocolateTypeId) VALUES('Raffaello', 100, 20, 3)
INSERT INTO Chocolate(Name, Weight, Price, ChocolateTypeId) VALUES('Havana', 100, 17, 2)

INSERT INTO Present(Title, Description, Price) VALUES('Christmas', 'Christmas present', 10)
INSERT INTO Present(Title, Description, Price) VALUES('Easter', 'Easter present', 15)
INSERT INTO Present(Title, Description, Price) VALUES('Birthday', 'Birthday present', 20)
-- add some data in Child table
INSERT INTO Child(Name, Surname, Age, Gender) VALUES
('John', 'Doe', 11, 'M'),
('Jane', 'Doe', 15, 'F'),
('John', 'Smith', 12, 'M'),
('Jane', 'Smith', 14, 'F')
-- add some data in ChocolatePresent table
INSERT INTO ChocolatePresent(ChocolateId, PresentId, Quantity, ExpirationDate) VALUES
(1, 1, 1, '2020-12-25'),
(2, 1, 2, '2020-12-25'),
(3, 1, 3, '2020-12-25'),
(4, 1, 4, '2020-12-25'),
(1, 2, 1, '2020-04-25'),
(2, 2, 2, '2020-04-25'),
(3, 2, 3, '2020-04-25'),
(4, 2, 4, '2020-04-25'),
(1, 3, 1, '2020-10-25'),
(2, 3, 2, '2020-10-25'),
(3, 3, 3, '2020-10-25'),
(4, 3, 4, '2020-10-25')
-- add some data in ChocolateChild table
INSERT INTO ChocolateChild(ChocolateId, ChildId, Quantity) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(1, 2, 1),
(2, 2, 2),
(3, 2, 3),
(4, 2, 4),
(1, 3, 1),
(2, 3, 2),
(3, 3, 3),
(4, 3, 4),
(1, 4, 1),
(2, 4, 2),
(3, 4, 3),
(4, 4, 4)


--
-- 2) Implement a stored procedure that receives a chocolate, a present, a quantity an expiration date and adds the chocolate to the present.
-- If the chocolate is already included in the present, the quantity and the expiration date are updated.
--
CREATE PROCEDURE AddChocolateToPresent
    @ChocolateId INT,
    @PresentId INT,
    @Quantity INT,
    @ExpirationDate DATE
AS
BEGIN
    IF EXISTS(SELECT * FROM ChocolatePresent WHERE ChocolateId = @ChocolateId AND PresentId = @PresentId)
    BEGIN
        UPDATE ChocolatePresent SET Quantity = @Quantity, ExpirationDate = @ExpirationDate WHERE ChocolateId = @ChocolateId AND PresentId = @PresentId
    END
    ELSE
    BEGIN
        INSERT INTO ChocolatePresent(ChocolateId, PresentId, Quantity, ExpirationDate) VALUES(@ChocolateId, @PresentId, @Quantity, @ExpirationDate)
    END
END
--run the procedure
EXEC AddChocolateToPresent 1, 1, 5, '2020-12-25'

--
-- 3) Create a view that shows the names of the chocolates included in all the presents. 

CREATE VIEW ChocolatesInAllPresents AS
SELECT Chocolate.Name FROM Chocolate
INNER JOIN ChocolatePresent ON Chocolate.ChocolateId = ChocolatePresent.ChocolateId
GROUP BY Chocolate.Name
HAVING COUNT(ChocolatePresent.PresentId) = (SELECT COUNT(PresentId) FROM Present)
--
-- 4) Implement a function that lists the names of the children that haven't received any chocolate.
--
CREATE FUNCTION ChildrenWithoutChocolate() RETURNS TABLE
AS
RETURN
(
    SELECT Name, Surname FROM Child
    WHERE ChildId NOT IN (SELECT ChildId FROM ChocolateChild)
)
--run the function
SELECT * FROM ChildrenWithoutChocolate()
