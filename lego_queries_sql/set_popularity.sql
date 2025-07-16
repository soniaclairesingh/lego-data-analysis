/*Most popular themes by set count*/
SELECT t.name AS theme_name, COUNT(*) AS set_count
FROM sets s
INNER JOIN themes t ON s.theme_id = t.id
GROUP BY t.name
ORDER BY set_count DESC
LIMIT 10;
