-- This script lists all cities contained in a database.
SELECT cities.id, cities.name, states.name
    FROM cities AS c
    INNER JOIN states AS s
    ON c.id=s.id
ORDER BY c.id;
