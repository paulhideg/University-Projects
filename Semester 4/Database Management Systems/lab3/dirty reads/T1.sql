--Dirty Reads T1
-- try to update and rollback after a 10s delay
BEGIN TRANSACTION
UPDATE ChessTitle SET title_name='NM'
WHERE tid=3
WAITFOR DELAY '00:00:10'
ROLLBACK TRANSACTION


