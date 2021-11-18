-- This script lists all shows contained in a database.
mysql -u root -p hbtn_0d_tvshows < hbtn_0d_tvshows.sql
SELECT * FROM hbtn_0d_tvshows
    WHERE genre_id>0
-- ORDER BY tv_shows.title AND tv_show_genres.genre_id
