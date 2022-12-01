-- listing all the records of second_table
-- the result displays score and then the name
-- in descending order
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
