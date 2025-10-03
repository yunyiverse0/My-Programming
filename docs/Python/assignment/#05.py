# 05 반복문

#method 1 - for 반복문
animal = ["dog", "duck", "pony", "donkey", "giraffe", "elephant", "cat"]

for i in animal:
  if len(i) <= 5:
    print(i)

#method2 - while 반복문
animal = ["dog", "duck", "pony", "donkey", "giraff", "elephant", "cat"]

i = 0  

while i < len(animal):          # 리스트 길이만큼 반복 (7로 잡으면 원소가 추가됐을 때 리스트를 다 못돎)
    if len(animal[i]) <= 5:   
        print(animal[i])
    i = i + 1                   # 인덱스 +1



