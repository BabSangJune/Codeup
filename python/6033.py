"""
날짜 : 2021.07.16
학습 : codeup python 기초 100제
제목 : 6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기(설명)(py)
문제 :
문자 1개를 입력받아 그 다음 문자를 출력해보자.
영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

예시
...
print(chr(n+1))

참고
숫자는 수를 표현하는 문자로서 '0' 은 문자 그 자체를 의미하고, 0은 값을 의미한다.

힌트
아스키문자표에서 'A'는 10진수 65로 저장되고 'B'는 10진수 66으로 저장된다.
따라서, 문자도 값으로 덧셈을 할 수 있다. 어떤 문자의 값에 1을 더하면 그 다음 문자의 값이 된다.

입력 : a
출력 : b
"""

a = ord(input()) # ord로 a를 유니코드 값으로 변환
print(chr(a+1)) # a + 1 하여 chr로 정수로 변환


