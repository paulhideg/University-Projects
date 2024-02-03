USE [SportPerformances]
GO

INSERT INTO [SportTypes] ([description]) VALUES
	('Outdoor'),
	('Indoor')
GO

INSERT INTO [Sports] ([name], [description], [location], [tid]) VALUES
	('Football', 'Team Sport', 'London', 1),
	('Basketball', 'Team Sport', 'New York', 2)
GO

INSERT INTO [Clubs] ([name], [opening_year], [stars]) VALUES
	('London Lions', 1920, 5),
	('New York Knicks', 1946, 4)
GO

INSERT INTO [Players] ([name], [surname], [date_of_birth], [gender], [sid]) VALUES
	('John', 'Doe', '1990-05-15', 'M', 1),
	('Jane', 'Doe', '1992-03-20', 'F', 2)
GO

INSERT INTO [Participations] ([pid], [cid], [fee], [enrollment_date]) VALUES
	(1, 1, 100.00, '2022-01-01'),
	(2, 2, 120.00, '2022-02-01')
GO

SELECT * FROM [SportTypes]
SELECT * FROM [Sports]
SELECT * FROM [Clubs]
SELECT * FROM [Players]
SELECT * FROM [Participations]
