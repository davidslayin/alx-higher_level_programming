-- listing the number of records with the same score
-- and displaying them in descending order in number alias
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
