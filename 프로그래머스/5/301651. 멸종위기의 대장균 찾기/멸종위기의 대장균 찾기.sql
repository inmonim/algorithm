WITH RECURSIVE ecoli_tree AS (
    SELECT
        id,
        parent_id,
        1 AS generation
    FROM ecoli_data
    WHERE parent_id IS NULL

    UNION ALL

    SELECT
        e.id,
        e.parent_id,
        t.generation + 1 AS generation
    FROM ecoli_data e
    JOIN ecoli_tree t
      ON e.parent_id = t.id
),
leaf_counts AS (
    SELECT
        t.generation,
        COUNT(*) AS count
    FROM ecoli_tree t
    LEFT JOIN ecoli_data c
      ON c.parent_id = t.id
    WHERE c.id IS NULL
    GROUP BY t.generation
)
SELECT
    count,
    generation
FROM leaf_counts
ORDER BY generation;