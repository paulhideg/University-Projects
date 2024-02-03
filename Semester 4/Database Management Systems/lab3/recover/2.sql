GO
CREATE OR ALTER PROCEDURE uspAddTacticTransactional (@tactic_id TINYINT, @tactic_name VARCHAR(30))
AS
	SET NOCOUNT ON;
	BEGIN TRAN 
		BEGIN TRY
			IF EXISTS (SELECT * FROM Tactic WHERE tactic_name=@tactic_name)
			BEGIN 
				RAISERROR('Tactic already exists',14,1)
			END
			INSERT INTO Tactic VALUES (@tactic_id, @tactic_name)
			INSERT INTO LogTable VALUES('add','tactic',GETDATE())
			COMMIT TRAN
		END TRY 
	BEGIN CATCH 
		ROLLBACK TRAN
		print 'Transaction rollbacked'
	END CATCH

GO
CREATE OR ALTER PROCEDURE uspAddPlayerTransactional (@player_id INT, @player_name VARCHAR(100), @title_id TINYINT, @club_id TINYINT)
AS
	SET NOCOUNT ON;
	BEGIN TRAN 
		BEGIN TRY 
			IF EXISTS (SELECT * FROM ChessPlayer WHERE player_name=@player_name AND title_id=@title_id AND club_id=@club_id)
			BEGIN
				RAISERROR('Player already added',14,1)
			END
			INSERT INTO ChessPlayer VALUES (@player_id,@player_name, @title_id, @club_id)
			INSERT INTO LogTable VALUES ('add', 'player',GETDATE())
			COMMIT TRAN
		END TRY
		BEGIN CATCH 
			ROLLBACK TRAN
			print 'Transaction rollbacked'
		END CATCH

GO
CREATE OR ALTER PROCEDURE uspAddTacticsHistoryTransactional (@player_id INT, @tactic_id INT)
AS
	SET NOCOUNT ON;

	BEGIN TRAN
		BEGIN TRY
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
				COMMIT TRAN
		END TRY

		BEGIN CATCH
			ROLLBACK TRAN
			print 'Transaction rollbacked'
		END CATCH
GO

--select * from ChessPlayer
--select * from Tactic

-- each of the three transactions are independent of the others
GO
CREATE OR ALTER PROCEDURE uspPerformAddsBadScenario
AS 
	EXEC uspAddPlayerTransactional 11,'Alex Popa',3,2 -- enter the already exists branch so this will fail
	EXEC uspAddTacticTransactional 6,'Berlin Defense' -- this will not 
	EXEC uspAddTacticsHistoryTransactional 11,5 -- this will fail because of the first fail i.e. there is no id 11

GO
CREATE OR ALTER PROCEDURE uspPerformAddsGoodScenario
AS 
	EXEC uspAddPlayerTransactional 14,'L.Ming',1,2  -- these 3 will all succeed
	EXEC uspAddTacticTransactional 8,'Spanish Opening'
	EXEC uspAddTacticsHistoryTransactional 14,8
GO

EXEC uspPerformAddsGoodScenario
EXEC uspPerformAddsBadScenario

--select * from LogTable
-- 4 entries were added to the log table, showing the 4 transactions which succeeded