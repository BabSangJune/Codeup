"""
날짜 : 2021.07.16
학습 : codeup python 기초 100제
제목 : 6029 : [기초-값변환] 16진 정수 입력받아 8진수로 출력하기(설명)(py)
문제 :
16진수를 입력받아 8진수(octal)로 출력해보자.

예시
a = input()
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)  #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

참고
8진법은 한 자리에 8개(0 1 2 3 4 5 6 7)의 문자를 사용한다.
8진수 10은 10진수의 8, 11은 9, 12는 10 ... 와 같다.

입력 : f
출력 : 17
"""

a = input()
n = int(a, 16)
print('%o' % n) # %x(16진수)로 문자열 변경 (문자열 포맷팅)