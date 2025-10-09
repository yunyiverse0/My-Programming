  # *
 # **
# ***

a = ' '
N = 3

for i in range(3): 
    for j in range(2 - i):
        print(a, end='')
    for j in range(i + 1):
        print('*', end='')
    print() 
