WITH mp AS (
    SELECT
        category,
        MAX(PRICE) AS MAX_PRICE
    FROM food_product
    WHERE
        category IN ('과자', '국', '김치', '식용유')
    GROUP BY
        category
    ORDER BY
        MAX_PRICE DESC
)

SELECT
    fp.category AS CATEGORY,
    mp.MAX_PRICE AS MAX_PRICE,
    fp.PRODUCT_NAME AS PRODUCT_NAME
FROM
    food_product AS fp
    JOIN mp ON fp.price = mp.MAX_PRICE
WHERE
    fp.category IN ('과자', '국', '김치', '식용유')
ORDER BY
    MAX_PRICE DESC