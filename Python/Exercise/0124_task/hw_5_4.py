''' 방법 (1) 내장함수 활용 '''
# def find_min_max(my_list):
#     min = sorted(my_list)
#     max = sorted(my_list, reverse=True)
#     return min[0], max[0]

# result = find_min_max([3, 1, 7, 2, 5])
# print(result)  # (1, 7)


''' 방법 (2) 리스트 메서드 활용 - 0124 수업 내용 '''
def find_min_max(my_list):
    my_list.sort()
    min = my_list.pop(0)
    max = my_list.pop()
    return min, max

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)


'''함수에 들어가기 전에 코드를 미리 짜보는 것도 추천!'''
# my_list = [3, 1, 7, 2, 5]

# my_list.sort()
# result_1 = my_list.pop(0)
# result_2 = my_list.pop()

# print(f'({result_1}, {result_2})')

'''주어진 변수명이 익숙하지 않다면 짧은 알파벳으로 직관적으로 해결해보자!'''
# def a(l):
#     min = sorted(l)
#     max = sorted(l, reverse=True)
#     return min[0], max[0]

# r = a([3, 2, 5])
# print(r)
