-- 코드를 입력하세요
SELECT
    ai.ANIMAL_ID,
    ai.ANIMAL_TYPE,
    ai.NAME
FROM
    ANIMAL_INS AS ai
    LEFT JOIN ANIMAL_OUTS AS ao ON ai.animal_id = ao.animal_id
WHERE
    ai.SEX_UPON_INTAKE LIKE 'Intact%'
    AND (ao.SEX_UPON_OUTCOME LIKE 'Spayed%' OR ao.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY
    ai.ANIMAL_ID