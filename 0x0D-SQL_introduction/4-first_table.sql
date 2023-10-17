--  script that creates a table called first_table in the current database in your MySQL server.
mysql -D your_database_name -e "CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));"
