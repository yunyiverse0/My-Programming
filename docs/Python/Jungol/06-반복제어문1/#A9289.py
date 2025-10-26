sum = 0
a = []

while True:
    N = int(input())
    if N % 2 == 0 and 1 <= N <= 5:
        sum += N
        a.append(N)
    if N > 5 or 1 > N:
      print(int(sum/len(a)))
      break


cnt = 0
tot = 0

while True:
    N = int(input())
    if N > 5 or N < 1:
        break
    if N % 2 == 0:
        tot += N
        cnt += 1

print(int(tot/cnt))
