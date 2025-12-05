-- 코드를 입력하세요
WITH staging AS (
    SELECT
        ui.user_id AS user_id,
        gender,
        YEAR(sales_date) as year,
        MONTH(sales_date) AS month
    FROM
        user_info AS ui
        JOIN online_sale AS os ON ui.user_id = os.user_id
    WHERE
        gender IS NOT NULL
)

SELECT
    year, month, gender, COUNT(DISTINCT user_id) AS users
FROM
    staging
GROUP BY
    year, month, gender
ORDER BY
    year, month, gender