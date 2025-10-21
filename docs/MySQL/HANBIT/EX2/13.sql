/*예제2-13 : IS, UPDATE*/
SELECT *
FROM 고객
WHERE 지역 IS NULL;     

SELECT *
FROM 고객
WHERE 지역 ='';

UPDATE 고객
SET 지역 = NULL
WHERE 지역 = '';


/* NULL인 값을 찾고 비운 후 빈 문자열을 NULL로 수정*/
