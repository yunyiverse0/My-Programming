/*예제2-4  ORDER BY 사용*/
SELECT 고객번호
      ,담당자명
	  ,도시
	  ,마일리지 AS 포인트
FROM 고객
WHERE 도시 = '서울특별시'
ORDER BY 마일리지 DESC;

/*ORDER BY : 결과를 특정 컬럼 기준으로 정렬*/


/*예제2-5  LIMIT*/
SELECT *
FROM 고객
LIMIT 3;

/*LIMIT : 결과에서 보여줄 행의 개수 제한*/


/*예제2-6  내림차순*/
SELECT *
FROM 고객
ORDER BY 마일리지 DESC
LIMIT 3;
