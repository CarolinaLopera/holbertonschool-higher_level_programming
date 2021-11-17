-- This script creates the table.
CREATE TABLE IF NOT EXISTS force_name (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256) NOT NULL);
