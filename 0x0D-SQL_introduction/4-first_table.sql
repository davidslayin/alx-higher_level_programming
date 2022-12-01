-- creating a table first_table
-- should not fail if it already exists
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
