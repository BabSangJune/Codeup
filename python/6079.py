"""
날짜 : 2021.07.25
학습 : codeup python 기초 100제
제목 : 6079 : [기초-종합] 언제까지 더해야 할까?(py)
문제 :
1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
계속 더하는 프로그램을 작성해보자.

즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.

입력 :
55

출력 :
10
"""

# for 문
# num = int(input())
# #일단 몇번 더했는지 저장할 변수
# cnt_num = 0
# #누적합 저장 할 변수
# tot_num = 0
#
# for nums in range(1, num+1): #1~num까지
#     tot_num += nums
#     cnt_num += 1
#     if tot_num >= num: #tot_num이 입력한 num보다 작거나 같으면
#         print(cnt_num) #출력하고
#         break #스톱

#while문
num = int(input())
cnt_num = 0
tot_num = 0

while tot_num < num:
    cnt_num += 1 #이게 밑으로가면 0부터 더해서 11이 나옴 주의
    tot_num += cnt_num

print(cnt_num)

"""
참고

"""