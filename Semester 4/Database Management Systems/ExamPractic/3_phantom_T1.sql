USE [SportPerformances]
GO

-- Create 4 scenarios that reproduce the following concurrency issues under pessimistic isolation
-- levels: dirty reads, non-repeatable reads, phantom reads, and a deadlock; you can use stored
-- procedures and / or stand-alone queries; find solutions to solve / workaround the concurrency
-- issues. (grade 9)

SELECT * FROM [SportTypes]

-- PHANTOM READS T1
BEGIN TRAN
WAITFOR DELAY '00:00:05'
INSERT INTO [SportTypes] ([description])
VALUES ('Phantom')
COMMIT TRAN

DELETE FROM [SportTypes] WHERE [description] = 'Phantom'
