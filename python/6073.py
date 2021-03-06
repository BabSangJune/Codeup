"""
날짜 : 2021.07.24
학습 : codeup python 기초 100제
제목 : 6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(py)
문제 :
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

while 조건식 :
  ...
  ...

반복 실행구조를 사용해 보자.

입력 :
5

출력 :
4
3
2
1
0
"""
n = int(input())

while n != 0:
    n -= 1
    print(n)


"""
참고
조건검사, 출력, 감소의 순서와 타이밍을 잘 생각해보자.
"""