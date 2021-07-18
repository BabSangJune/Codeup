"""
날짜 : 2021.07.18
학습 : codeup python 기초 100제
제목 : 6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기(설명)(py)
문제 :
정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

예시
...
c = int(a) - int(b)
print(c)

참고
수 - 수는 차(subtraction)가 계산된다.

입력 : 123 -123
출력 : 246
"""

a, b = input().split()
c = int(a) - int(b)
print(c)