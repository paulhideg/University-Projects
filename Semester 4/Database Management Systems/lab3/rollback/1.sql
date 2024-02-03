GO
DROP TABLE IF EXISTS LogTable 
CREATE TABLE LogTable(
	Lid INT IDENTITY PRIMARY KEY,
	TypeOperation VARCHAR(50),
	TableOperation VARCHAR(50),
	ExecutionDate DATETIME
);

GO
-- check for duplicates
CREATE OR ALTER PROCEDURE uspAddTactic (@tactic_id TINYINT, @tactic_name VARCHAR(30))
AS
	SET NOCOUNT ON;
	IF EXISTS (SELECT * FROM Tactic WHERE tactic_name=@tactic_name)
	BEGIN 
		RAISERROR('Tactic already exists',14,1)
	END
	INSERT INTO Tactic VALUES (@tactic_id,@tactic_name)
	INSERT INTO LogTable VALUES('add','tactic',GETDATE())
	
GO

-- check for duplicates
CREATE OR ALTER PROCEDURE uspAddPlayer (@player_id INT, @player_name VARCHAR(100), @title_id TINYINT, @club_id TINYINT)
AS
	SET NOCOUNT ON
	IF EXISTS (SELECT * FROM ChessPlayer WHERE player_name=@player_name AND title_id=@title_id AND club_id=@club_id)
	BEGIN
		RAISERROR('Player already added',14,1)
	END
	INSERT INTO ChessPlayer VALUES (@player_id,@player_name, @title_id, @club_id)
	INSERT INTO LogTable VALUES ('add', 'player',GETDATE())
GO

-- check that player_id is ok, tactic_id is ok  & the pair doesn't already exist 
CREATE OR ALTER PROCEDURE uspAddTacticsHistory (@player_id INT, @tactic_id INT)
AS
	SET NOCOUNT ON;

	IF NOT EXISTS (SELECT * FROM ChessPlayer P WHERE P.player_id = @player_id)
	BEGIN
			RAISERROR('Invalid player id', 14, 1)
	END
	
	IF NOT EXISTS (SELECT * FROM Tactic T WHERE T.tactic_id = @tactic_id)
	BEGIN
		RAISERROR('Invalid tactic id', 14, 1)
	END
	
	IF EXISTS (SELECT * FROM TacticsHistory TH WHERE TH.player_id = @player_id AND TH.tactic_id = @tactic_id)
	BEGIN
		RAISERROR('Tactic + player already logged in history', 14, 1)
	END

	INSERT INTO TacticsHistory VALUES (@player_id, @tactic_id);
	print 'Added!'
	--log the transaction
	INSERT INTO LogTable VALUES('add','TacticsHistory',GETDATE())
GO


GO
CREATE OR ALTER PROCEDURE uspAddRollbackScenario 
AS
	BEGIN TRAN
	BEGIN TRY 
		EXEC uspAddPlayer 11,'Alex Popa',3,2 -- enter the already exists branch so this will fail, so the next two will never be reached
		EXEC uspAddTactic 6,'Berlin Defense' 
		EXEC uspAddTacticsHistory 11,5 
		COMMIT TRAN
	END TRY
	BEGIN CATCH -- if one transaction fails i.e. throws exception, rollback everything
		ROLLBACK TRAN
		RETURN
	END CATCH

GO
CREATE OR ALTER PROCEDURE uspAddCommitScenario
AS
	BEGIN TRAN
	BEGIN TRY 
		EXEC uspAddPlayer 20,'Dani Pop',2,2 -- all 3 will succeed
		EXEC uspAddTactic 20,'English Game' 
		EXEC uspAddTacticsHistory 20,20 
		COMMIT TRAN
	END TRY
	BEGIN CATCH 
		ROLLBACK TRAN
		RETURN
	END CATCH

GO
EXEC uspAddRollbackScenario
EXEC uspAddCommitScenario

--3 entries will be added to the log table
--select * from LogTable
