USE [master]
GO

ALTER DATABASE [SportPerformances] SET SINGLE_USER WITH ROLLBACK IMMEDIATE
GO

DROP DATABASE IF EXISTS [SportPerformances]
CREATE DATABASE [SportPerformances];
GO

USE [SportPerformances];
GO

CREATE TABLE [SportTypes] (
    [tid] INT PRIMARY KEY IDENTITY,
    [description] NVARCHAR(255) NOT NULL
);
GO

CREATE TABLE [Sports] (
    [sid] INT PRIMARY KEY IDENTITY,
    [name] NVARCHAR(50) NOT NULL,
    [description] NVARCHAR(255),
    [location] NVARCHAR(50) NOT NULL,
    [tid] INT FOREIGN KEY REFERENCES [SportTypes]([tid])
);
GO

CREATE TABLE [Clubs] (
    [cid] INT PRIMARY KEY IDENTITY,
    [name] NVARCHAR(50) NOT NULL,
    [opening_year] INT CHECK ([opening_year] > 1800 AND [opening_year] <= YEAR(GETDATE())),
    [stars] INT CHECK ([stars] >= 0)
);
GO

CREATE TABLE [Players] (
    [pid] INT PRIMARY KEY IDENTITY,
    [name] NVARCHAR(50) NOT NULL,
    [surname] NVARCHAR(50) NOT NULL,
    [date_of_birth] DATE NOT NULL,
    [gender] CHAR(1) CHECK ([gender] IN ('F', 'M', 'O')),
    [sid] INT FOREIGN KEY REFERENCES [Sports]([sid])
);
GO

CREATE TABLE [Participations] (
    [pid] INT FOREIGN KEY REFERENCES [Players]([pid]),
    [cid] INT FOREIGN KEY REFERENCES [Clubs]([cid]),
    CONSTRAINT [PK_Participations] PRIMARY KEY ([pid], [cid]),

    [fee] FLOAT(24) NOT NULL CHECK ([fee] >= 0),
    [enrollment_date] DATE NOT NULL
);
GO
