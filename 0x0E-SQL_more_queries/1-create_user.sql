-- creates the MySQL server user user_0d_1.
-- user_0d_1 has all privileges on MySQL server
-- The user_0d_1 password set to user_0d_1_pwd
-- If the user user_0d_1 already exists, script does not fail
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVIlEGES ON *.* TO user_0d_1@localhost;
FLUSH PRIVILEGES;
