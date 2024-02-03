DROP DATABASE IF EXISTS DBMS_Exam
CREATE DATABASE DBMS_Exam;
GO

go 
use DBMS_Exam

CREATE TABLE Player (
    pid INT PRIMARY KEY IDENTITY,
    name NVARCHAR(50) NOT NULL,
    surname NVARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender CHAR(1) CHECK ([gender] IN ('F', 'M'))
);

CREATE TABLE CardType (
    ctid INT PRIMARY KEY IDENTITY,
    description NVARCHAR(255) NOT NULL
);

CREATE TABLE Card (
    cid INT PRIMARY KEY IDENTITY,
	date_of_purchasing DATE NOT NULL,
	tracer NVARCHAR(50) NOT NULL,
	due_date DATE NOT NULL,
    ctid INT FOREIGN KEY REFERENCES CardType(ctid),
	pid INT FOREIGN KEY REFERENCES Player(pid)
);

CREATE TABLE Team (
    tid INT PRIMARY KEY IDENTITY,
    name NVARCHAR(50) NOT NULL,
    location NVARCHAR(50),
    nr_of_members INT NOT NULL
);

CREATE TABLE Contract (
    pid INT FOREIGN KEY REFERENCES Player(pid),
    tid INT FOREIGN KEY REFERENCES Team(tid),
    CONSTRAINT [PK_Contract] PRIMARY KEY (pid, tid),
	start_date DATE NOT NULL,
    end_date DATE NOT NULL
);
