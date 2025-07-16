/*Average parts per set over time*/
SELECT year, AVG(num_parts) AS avg_parts
FROM sets
GROUP BY year
ORDER BY year;