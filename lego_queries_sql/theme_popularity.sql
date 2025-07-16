/*Theme popularity over time*/
SELECT t.name AS theme_name, s.year, COUNT(*) AS set_count
FROM sets s
JOIN themes t ON s.theme_id = t.id
GROUP BY t.name, s.year
ORDER BY s.year, set_count DESC;