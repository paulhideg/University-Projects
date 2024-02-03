-- in order to be able to replicate the update conflict we need to allow snapshots 
ALTER DATABASE Chess4 SET ALLOW_SNAPSHOT_ISOLATION ON

WAITFOR DELAY '00:00:10'
BEGIN TRAN
UPDATE ChessTitle SET title_name='Champion' WHERE tid=10;
--title name is now Champion
WAITFOR DELAY '00:00:10'
COMMIT TRAN

--ALTER DATABASE Chess4 SET ALLOW_SNAPSHOT_ISOLATION OFF

--insert into ChessTitle(tid, title_name) values (10, 'Retired') 
--select * from ChessTitle
--update ChessTitle set title_name='Retired' where tid=10;