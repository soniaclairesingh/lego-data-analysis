/*Average Parts per Theme*/
SELECT themes.name AS themes_name, ROUND(AVG(sets.num_parts),3) AS avg_parts
FROM sets
INNER JOIN themes ON sets.theme_id = themes.id
GROUP BY themes.name
ORDER BY avg_parts DESC;