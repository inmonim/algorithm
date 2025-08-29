-- 코드를 입력하세요
SELECT
    b.book_id,
    a.author_name,
    DATE_FORMAT(b.published_date, '%Y-%m-%d') AS published_date
FROM
    BOOK AS b
    JOIN AUTHOR AS a ON b.author_id = a.author_id
WHERE
    b.category = '경제'
ORDER BY
    b.published_date