-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- cities id INT unique, auto generated, not null and is a primary key, state_id INT, not null and must be a FOREIGN KEY that references to id of the states table, name VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_od_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
