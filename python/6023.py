"""
날짜 : 2021.07.16
학습 : codeup python 기초 100제
제목 : 6023 : [기초-입출력] 시분초 입력받아 분만 출력하기(py)
문제 :
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
------

시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.

어떻게 분만 출력해야 할지 주의 깊게 생각해야한다.


입력 : 17:23:57
출력 : 23
"""

time = input().split(':')
print(time[1])