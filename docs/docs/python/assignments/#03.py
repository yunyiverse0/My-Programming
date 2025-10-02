# 03 다양한 연산자 

alp = input("알파벳을 입력하세요 :")

if "A" >= alp >= "Z":
  print(f"당신이 입력한 문자는 대문자 입니다")
elif "a" >= alp >= "z":
  print(f"당신이 입력한 문자는 소문자 입니다")
else:
  print(f"당신이 입력한 문자는 알파벳이 아닙니다")
