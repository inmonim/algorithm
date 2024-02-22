SELECT DISTINCT user_id, product_id
FROM ONLINE_SALE x
WHERE 2 <= (SELECT COUNT(*)
              FROM ONLINE_SALE y
             WHERE x.user_id = y.user_id AND x.product_id = y.product_id)
ORDER BY USER_ID, PRODUCT_ID DESC