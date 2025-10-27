def D():
    x, y = map(int,input().split())
    a = x + y
    if x >= y:
        b = x - y
    else:
        b = y - x
    return a, b  #여러 값이 return되면 튜플로 반환됨 ( 하나일 땐 숫자 혹은 문자열로 반환)

a, b = D()    #튜플을 언패킹 해줌 -> a와 b에 각각 D()의 결과인 (a, b)를 a와 b에 쥐어줌

print('두 수의 합 =',a)
print('두 수의 차 =',b)
