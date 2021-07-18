"""
날짜 : 2021.07.19
학습 : codeup python 기초 100제
제목 : 6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기(설명)(py)
문제 :
정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.

예시
n = int(input())
print(bool(n))

입력 :
0 1
출력 :
True
"""

a = input()
print(bool(int(a)))


"""
참고
bool( ) 을 이용하면 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력해준다.
식이나 값을 계산해서 결과값이 만들어지는 것을 평가(evaluate)라고 한다. 

python 언어에서 정수값 0은 False(거짓)로 평가되고, 그 외의 값들은 모두 True(참)로 평가된다.
** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.
"""