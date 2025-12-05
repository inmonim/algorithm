# WITH g2 AS 

SELECT
    g3.id AS id
FROM
    (
    SELECT
        g2.id, g2.parent_id
    FROM
        ecoli_data AS g1 JOIN ecoli_data AS g2 ON g1.parent_id IS NULL and g2.parent_id = g1.id
) AS g2 JOIN ecoli_data AS g3 ON g3.parent_id = g2.id
ORDER BY
    id