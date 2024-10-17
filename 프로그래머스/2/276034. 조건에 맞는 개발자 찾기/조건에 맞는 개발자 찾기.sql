-- 코드를 작성해주세요

SELECT DISTINCT dp.ID, dp.EMAIL, dp.FIRST_NAME, dp.LAST_NAME
FROM (SELECT NAME, CODE
        FROM SKILLCODES
        WHERE NAME IN ('Python', 'C#')) cd JOIN DEVELOPERS dp
WHERE dp.SKILL_CODE & cd.CODE
ORDER BY dp.ID;