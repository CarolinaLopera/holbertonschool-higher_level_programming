-- This script creates a database and a table.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT PRIMARY KEY UNIQUE NOT NULL GETDATE(),
    name VARCHAR(256) NOT NULL
);