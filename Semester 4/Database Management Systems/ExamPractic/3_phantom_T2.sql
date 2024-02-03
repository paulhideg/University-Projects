USE [SportPerformances]
GO

SELECT * FROM [SportTypes]

-- PHANTOM READS T2
-- in the second select we will see the "phantom" = the record which shouldn't be there
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ
BEGIN TRAN
SELECT * FROM [SportTypes]
WAITFOR DELAY '00:00:05'
SELECT * FROM [SportTypes]
COMMIT TRAN

-- Solution: T1: delay + insert + commit, T2: select + delay + select -> the new inserted values are not
-- visible at the end of T2 and T1, only if we make a new select and test it.
-- neither selects will show the inserted record from T1 
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
BEGIN TRAN
SELECT * FROM [SportTypes]
WAITFOR DELAY '00:00:05'
SELECT * FROM [SportTypes]
COMMIT TRAN
