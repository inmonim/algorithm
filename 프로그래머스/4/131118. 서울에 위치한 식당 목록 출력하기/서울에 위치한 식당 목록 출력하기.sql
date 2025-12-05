WITH score AS (
    SELECT
        rest_id,
        ROUND(SUM(review_score) / COUNT(*) , 2) AS score
    FROM
        REST_REVIEW
    GROUP BY
        rest_id
)

SELECT
    ri.rest_id AS REST_ID,
    rest_name AS REST_NAME,
    food_type AS FOOD_TYPE,
    favorites AS FAVORITES,
    address AS ADDRESS,
    score AS SCORE
FROM
    REST_INFO AS ri
    JOIN score AS s ON ri.rest_id = s.rest_id
WHERE
    address LIKE '서울%'
ORDER BY
    score DESC, favorites DESC