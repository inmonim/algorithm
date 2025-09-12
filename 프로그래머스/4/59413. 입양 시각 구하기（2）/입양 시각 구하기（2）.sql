WITH RECURSIVE hours(h) AS (
  SELECT 0
  UNION ALL
  SELECT h + 1 FROM hours WHERE h < 23
),

hc AS (
    SELECT
        EXTRACT(HOUR FROM datetime) AS dt,
        COUNT(*) as dt_c
    FROM
        ANIMAL_OUTS
    GROUP BY
        dt
)

SELECT
    hours.h AS HOUR,
    IFNULL(hc.dt_c, 0) AS COUNT
FROM hours
    LEFT JOIN hc ON hours.h = hc.dt

