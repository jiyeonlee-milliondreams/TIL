# ''' 일반 알고리즘 구현 '''
# N = 370 // 7 + 1
# calender = [[0] * 7 for _ in range(N)]
#
# calender[0][4] = [1, 1]
# calender[0][5] = [1, 2]
# calender[0][6] = [1, 3]
#
# month = 1
# number = 4
# month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# for i in range(1, N):
#     for j in range(7):
#             if number < month_days[month]:
#                 calender[i][j] = [month, number]
#                 number += 1
#             elif number == month_days[month]:
#                 calender[i][j] = [month, number]
#                 number = 1
#                 if month < 12:
#                     month += 1
#                     month_start_day_idx.append([i, j])
#                 else:
#                     break   # for j
#
# print(calender)
#
# a = int(input())
# b = int(input())
# day_lst = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
# day = day_lst[0]
#
# for i in range(N):
#     for j in range(7):
#         if calender[i][j] == [a, b]:
#             day = day_lst[j]
#
# print(day)

'''
# 함수 구현
def solution(a, b):
    # calender 만들기
    ##  이차원 배열 만들기
    N = 370 // 7 + 1
    calender = [[0] * 7 for _ in range(N)]

    ## 첫 행은 별도로 채워주기
    calender[0][4] = [1, 1]
    calender[0][5] = [1, 2]
    calender[0][6] = [1, 3]

    ## 두 번째 행부터 calender 채우기
    month = 1  # 월 초기값 1
    number = 4  # 일 초기값 4
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 12월에 맞춰 0 추가

    for i in range(1, N):
        for j in range(7):  # 7일 동안
            if number < month_days[month]:  # 날짜가 month_days를 미만이면
                calender[i][j] = [month, number]
                number += 1  # 1 더해서 캘린더 채우기
            elif number == month_days[month]:  # 날찌기 month_days와 같으면
                calender[i][j] = [month, number]
                number = 1  # 1 더해서 캘린더 채우고
                if month < 12:  # 12월 전이라면 월 + 1
                    month += 1
                else:  # 12월이라면 반복 중지
                    break  # for j

    # 열 인덱스와 맞는 요일 리스트 생성
    day_lst = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = day_lst[0]  # 초기값 월요일로 설정

    # [a, b] 찾아서 요일 반환
    for i in range(N):
        for j in range(7):
            if calender[i][j] == [a, b]:
                day = day_lst[j]
    return day


print(solution(5, 24))
'''

'''최적화'''

def day_of_week(month, day):
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_lst = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    date = day
    for i in range(1, month):
        date += month_days[i]
    answer = day_lst[date % 7]

    return answer

print(day_of_week(1, 1))
print(day_of_week(5, 24))

