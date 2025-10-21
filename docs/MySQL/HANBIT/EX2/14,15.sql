/*예제2-14 : IN, ON - 특정 직위만 조회*/
SELECT 고객번호
	  ,담당자명
      ,담당자직위
FROM 고객
WHERE 담당자직위 = '영업 과장'
OR 담당자직위 = '마케팅 과장';

SELECT 고객번호
      ,담당자명
      ,담당자직위
FROM 고객
WHERE 담당자직위 IN ('영업 과장', '마케팅 과장');

/*예제2-15*/
SELECT 담당자명
      ,마일리지
FROM 고객
WHERE 마일리지 >= 100000
AND 마일리지 <= 200000;

SELECT 담당자명
      ,마일리지
FROM 고객
WHERE 마일리지 BETWEEN 100000 AND 200000;
