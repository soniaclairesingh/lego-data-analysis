/*Largest lego set by part count*/
SELECT name, num_parts, year
FROM sets
ORDER BY num_parts DESC
LIMIT 10;