# 04 조건문 01

# 주택용, 공업용, 산업용 순서
# 기본 요금 : 910, 1600, 7300
# Kwh 전력량 요금 : 88, 182, 275
# 총 요금=기본요금+(사용량(kWh)×단가)

typ = int(input("(1)주택용 (2)공업용 (3)산업용 :"))
use = int(input("전력 사용량(kwh) :"))

if typ == 1:
  fee = 910+use*88
elif typ == 2:
  fee = 1600+use*182
elif typ == 3:
  fee = 7300+use*275
else:
  print("입력하신 값을 다시 확인해주세요.")

print(f"""용도: {typ}
사용량: {use}
전기요금 : {fee:,.2f}""")
