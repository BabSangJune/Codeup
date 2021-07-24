"""
날짜 : 2021.07.24
학습 : codeup python 기초 100제
제목 : 6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)
문제 :
영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

예시
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1
입력 :
f

출력 :
a b c d e f
"""

word = ord(input())
first_a = ord('a')

while first_a <= word:
    print(chr(first_a), end=' ')
    first_a += 1


"""
참고
알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다.
print(..., end=' ') 와 같이 작성하면 값 출력 후 공백문자 ' '를 출력한다. 즉, 마지막에 줄을 바꾸지 않고 빈칸만 띄운다.
(end='\n'로 작성하거나 생략하면, 값을 출력한 후 마지막(end)에 줄바꿈(newline)이 된다.)
"""