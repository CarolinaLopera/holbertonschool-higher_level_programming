--
SELECT score, COUNT(score) AS times
    FROM second_table
    GROUP BY score
    ORDER BY score DESC
