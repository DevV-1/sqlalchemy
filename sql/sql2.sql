SELECT
    c.id, 
    c.fname,
    SUM (i.id) AS total
From invoice i
LEFT JOIN customer c on i.customer_id = c.id
GROUP BY c.id, c.fname
ORDER BY total DESC
LIMIT :limit;