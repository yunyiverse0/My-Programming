/*예제2-12 : UNION*/
SELECT 고객번호
      ,담당자명
	  ,마일리지
      ,도시
FROM 고객
WHERE 도시 = '부산광역시'
UNION
SELECT 고객번호
      ,담당자명
      ,마일리지
      ,도시
FROM 고객
WHERE 마일리지 < 1000
ORDER BY 1;

/*UNION : 두 결과를 합치는 것 (앞 뒤의 SELECT문은 완전해야함)*/
