-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci including thr Table first_table and Field name in first_table
-- Convert the database to UTF8
ALTER DATABASE
    hbtn_0c_0
	CHAR SET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;
ALTER TABLE
    first_table
	CONVERT TO CHAR SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
ALTER TABLE
    first_table
	MODIFY name
	VARCHAR(256)
	CHAR SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
