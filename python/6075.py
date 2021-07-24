"""
날짜 : 2021.07.24
학습 : codeup python 기초 100제
제목 : 6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1(py)
문제 :
정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

입력 :
4

출력 :
0
1
2
3
4
"""

num = int(input())
first_num = 0

while first_num <= num:
    print(first_num)
    first_num += 1

"""
참고
"""