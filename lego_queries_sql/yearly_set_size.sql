/*Yearly Trends of Set Size - how the average number of parts per set changes by year */
SELECT year, ROUND(AVG(num_parts),3) AS avg_parts
FROM sets
GROUP BY year
ORDER BY avg_parts DESC;
