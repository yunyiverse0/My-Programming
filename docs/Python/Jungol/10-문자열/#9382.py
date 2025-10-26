A = "apple orange banana"
B = "  Hello world!  "

# 1️⃣ 단어를 공백 기준으로 나눠 뒤집기
words = A.split()        # ['apple', 'orange', 'banana']
words.reverse()          # ['banana', 'orange', 'apple']
print('_'.join(words))   # banana_orange_apple

# 2️⃣ 앞뒤 공백 제거 전후 출력
print(B)
print(B.strip())
