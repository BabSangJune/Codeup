"""
날짜 : 2021.07.24
학습 : codeup python 기초 100제
제목 : 6077 : [기초-종합] 짝수 합 구하기(설명)(py)
문제 :
정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

예시
#다음 코드는 홀 수만 더해 출력한다.
n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==1 :
    s += i

print(s)

입력 :
5

출력 :
6
"""

#for in range
# num = int(input())
# result = 0
#
# for nums in range(1, num+1):
#     if nums % 2 == 0:
#         result += nums
#
# print(result)

#while
num = int(input())
cnt = 0
result = 0
while cnt <= num:

    if cnt % 2 == 1:
        result += cnt
    cnt += 1
print(result)

"""
참고
while 이나 for 반복실행구조를 이용할 수 있다.
다른 방법이나 while 반복실행구조를 이용해서도 성공시켜 보자.
"""