# 실수 2개를 입력받아 합계를 구하고 각각 소수 셋째 자리에서 반올림하여 둘째 자리까지 한 줄에 출력하는 프로그램을 작성하시오.

f = open("input.txt", "r") 
F = open("output.txt", "w+") 

flist = f.readline().split()

for i in f:
    n = round(float(i),3) #file에서 나온 데이터이기에 문자열임 -> 실수로 바꿔줌 / 소수 셋째 자리에서 반올림함 
    flist.append(n)

hap = float(flist[0]) + float(flist[1])
Hap = round(hap, 3)
flist.append(Hap)

for i in flist:
    n = float(i)
    if i != Hap:
        F.write(f'{n:.2f}'+' ') 
    else:
        F.write(f'{n:.2f}')

f.close()
F.close()
