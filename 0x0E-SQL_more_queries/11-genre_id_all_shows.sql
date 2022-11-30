-- list all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_shows.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
