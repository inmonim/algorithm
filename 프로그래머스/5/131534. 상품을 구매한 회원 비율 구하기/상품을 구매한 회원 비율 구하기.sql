-- 코드를 입력하세요
WITH t1 AS (
    SELECT
        user_id AS user_id
    FROM
        user_info
    WHERE
        joined BETWEEN '2021-01-01' AND '2021-12-31'
),

t2 AS (
    SELECT
        t1.user_id,
        YEAR(os.sales_date) AS y,
        MONTH(os.sales_date) AS m
    FROM
        t1
        JOIN online_sale AS os ON t1.user_id = os.user_id
)

SELECT
    y AS YEAR,
    m AS MONTH,
    COUNT(DISTINCT user_id) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(user_id) FROM t1), 1) AS PUCHASED_RATIO
FROM
    t2
GROUP BY
    y, m