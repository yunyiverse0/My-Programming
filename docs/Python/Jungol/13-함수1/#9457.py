K = int(input())

def f(x, y, z):
    X = K - x if K >= x else x - K
    Y = K - y if K >= y else y - K
    Z = K - z if K >= z else z - K

    return X, Y, Z

a,b,c = map(int,input().split())    #인자값을 먼저 받아야함
f(a,b,c)

X, Y, Z = f(a, b, c)    

for i in (X, Y, Z):
  print(i)  
