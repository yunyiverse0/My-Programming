/*예제2-16*/
SELECT *
FROM 고객
WHERE 도시 LIKE '%광역시'
AND (고객번호 LIKE '_C%' OR 고객번호 LIKE '__C%');

/*'_' : 한 글자 대체
  '%' : 여러글자 대체*/
