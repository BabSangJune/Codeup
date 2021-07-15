"""
날짜 : 2021.07.16
학습 : codeup python 기초 100제
제목 : 6024 : [기초-입출력] 단어 2개 입력받아 이어 붙이기(설명)(py)
문제 :
알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
순서대로 붙여 출력하는 프로그램을 작성해보자.

예시
w1, w2 = input().split()
s = w1 + w2
print(s)

참고
단어는 문자(character)들로 만든다.
문자들로 구성된 문장을 문자열(string)이라고 부른다.
문자열에는 공백문자(' ')가 포함될 수 있는데,
문자 1개는 길이가 1인 문자열이라고 할 수 있고, 공백문자(' ')가 없는 문자열은 단어(word)라고 할 수 있다.

일반적인 문장들은 공백으로 구분된 단어들로 만들어지기 때문에,
공백문자로 구분된 문장에서 단어를 잘라내기 위해서는 공백문자(' ')를 기준으로 자르면 된다.
키보드로 입력되는 것들은 기본적으로 문자열로 인식되고, 문자열끼리 더하기(+)를 실행하면,
두 문자열을 합쳐 연결한(concatenate) 결과를 만들어 낸다.

입력 : hello world
출력 : helloworld
"""

w1, w2 = input().split()
s = w1 + w2

print(s)