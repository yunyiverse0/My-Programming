# N = 3

#
# #
# # #
  # #
    #


N = int(input())

for i in range(1, N + 1):
    for j in range(1, i + 1):
        print('#', end=' ')
    print()
for i in range(1, N + 1):
    print('  ' * i, end='')          
    for j in range(N - i, 0, -1):
        print('#', end=' ')
    print()
