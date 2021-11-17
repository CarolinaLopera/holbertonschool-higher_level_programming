-- This script creates a database and a table.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
