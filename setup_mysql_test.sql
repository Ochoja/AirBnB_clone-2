-- Prepare a MySQL server for the project
-- Create DB
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Set password for user
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- Grant privileges
GRANT ALL PRIVILEGES ON hbhb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant privileges
GRANT SELECT ON performance_schema TO 'hbnb_test'@'localhost';
