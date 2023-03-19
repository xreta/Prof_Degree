SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'rfam'
GROUP BY column_name
HAVING COUNT(DISTINCT table_name) > 1;
