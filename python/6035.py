"""
날짜 : 2021.07.18
학습 : codeup python 기초 100제
제목 : 6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기(설명)(py)
문제 :
실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

예시
...
m = float(f1) * float(f2)
print(m)

참고
수 * 수는 곱(multiplication)이 계산된다.

입력 : 0.5 0.2
출력 : 1.0
"""

a, b = input().split()
c = float(a) * float(b)
print(c)