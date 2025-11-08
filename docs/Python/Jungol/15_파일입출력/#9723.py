# 3개의 정수를 입력받아 합계와 평균을 구하여 출력하되 평균은 정수부분만 출력하고 나머지를 예와 같이 출력하는 프로그램을 작성하시오.

with open("input.txt", "r") as f, open("output.txt", "w+") as F:
    a = [int(i) for i in f.readline().split()]
    A = []
    hap = sum(a)
    avg = int( hap / len(a))
    rem = hap % len(a)
    A.append(hap), A.append(str(avg)+'...'+str(rem))

    for i in A:
        if A != avg:
            F.write(str(i) + ' ')
        else:
            F.write(str(i))
