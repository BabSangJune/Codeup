"""
날짜 : 2021.07.16
학습 : codeup python 기초 100제
제목 : 6022 : [기초-입출력] 연월일 입력받아 나누어 출력하기(설명)(py)
문제 : 
6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

참고
s = input()
print(s[0:2])

를 실행하면 0번째 문자부터 1번째 문자까지 잘라 출력한다.
s[a:b] 라고 하면, s라는 단어에서 a번째 문자부터 b-1번째 문자까지 잘라낸 부분을 의미한다.
다른 자르기 방법도 있다.

입력 : 200304
출력 : 20 03 04
"""


date = input()
print(date[0:2], date[2:4], date[4:6])


"""
6자리 숫자로 이루어진 연월일이 입력된다.
년도 월 일을 공백을 구분해 한 줄로 출력한다.
-> 슬라이싱하기 위해 str형으로 입력받는다.
-> for 반복문 + 슬라이싱으로 년도, 월, 일을 구분한다.
-> list + join + print로 list내의 요소들을 공백을 기준으로 출력한다.
코드💻
yymmdd = str(input())
result = []
cnt = 0

for _ in range(3):
    result.append(yymmdd[cnt:cnt+2])
    cnt += 2

print(" ".join(result))
"""