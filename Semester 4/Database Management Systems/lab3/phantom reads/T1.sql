--phantom problem T1
BEGIN TRAN 
WAITFOR DELAY '00:00:04'
INSERT INTO ChessTitle(tid, title_name) VALUES (5,'Beginner')
COMMIT TRAN

--DELETE FROM ChessTitle WHERE tid=5