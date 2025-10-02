# 02 자료형과 연산자

crg = 6450

a = crg // 500; crg %= 500
b = crg // 100; crg %= 100
c = crg // 50; crg %= 50
d = crg // 10; crg %= 10
# print(a,b,c,d)

print(f"""거스름돈 : {crg}원 
500원짜리 : {a}개 
100원짜리 : {b}개 
50원짜리 : {c}개 
10원짜리 : {d}개""")
