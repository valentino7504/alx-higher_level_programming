-- lists all the genres of dexter
SELECT tv_genres.name AS name
FROM tv_genres
WHERE tv_genres.id IN (
    SELECT genre_id 
    FROM tv_show_genres 
    WHERE tv_show_genres.show_id=(
        SELECT id 
        FROM tv_shows 
        WHERE tv_shows.title="Dexter"
    )
)
ORDER BY name ASC;
