-- 코드를 입력하세요
SELECT a.FLAVOR
  FROM FIRST_HALF a JOIN ICECREAM_INFO b ON (a.FLAVOR = b.FLAVOR)
 WHERE a.total_order >= 3000 AND b.ingredient_type = 'fruit_based'