"""
날짜 : 2021.07.18
학습 : codeup python 기초 100제
제목 : 6036 : [기초-산술연산] 단어 여러 번 출력하기(설명)(py)
문제 :
단어와 반복 횟수를 입력받아 여러 번 출력해보자.

예시
w, n = input().split()
print(w*int(n))

참고
문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.

입력 : love 3
출력 : lovelovelove
"""

w, n = input().split()
print(w * int(n))