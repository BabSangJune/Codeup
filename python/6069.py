"""
날짜 : 2021.07.21
학습 : codeup python 기초 100제
제목 : 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(py)
문제 :
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?

입력 :
A
출력 :
best!!!
"""

score = input()

if score == 'A':
    print('best!!!')
elif score == 'B':
    print('good!!')
elif score == 'C':
    print('run!')
elif score == 'D':
    print('slowly~')
else:
    print('what?')

