-- This script lists all cities contained in a database.
SELECT id, name FROM cities
    INNER JOIN states USING (name);
ORDER BY id;
