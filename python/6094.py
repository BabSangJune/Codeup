"""
날짜 : 2021.08.01
학습 : codeup python 기초 100제
제목 : 6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)
문제 :
정보 선생님은 오늘도 이상한 출석을 부른다.

영일이는 오늘도 다른 생각을 해보았다.
출석 번호를 다 부르지는 않은 것 같은데... 가장 빠른 번호가 뭐였지?

출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

단,
첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다.
음수(-) 번호, 0번 번호도 있을 수 있다.

입력 :
10
10 4 2 3 6 6 7 9 8 5

출력 :
2
"""

how_many_call = int(input())
numbers = input().split()

for i in range(how_many_call):
    numbers[i] = int(numbers[i])

result = numbers[0]
for j in numbers: 
    if result >= j: #j가 numbers 보다 크거나 같으면
        result = j #j를 result에 저장

print(result)


"""
참고
리스트에 출석 번호를 기록해 두었다가, 그 중에서 가장 작은 값을 찾아내면 된다.
그런데, 가장 작은 값은 어떻게 어떤 것과 비교하고, 어떻게 찾아야 할까?
"""