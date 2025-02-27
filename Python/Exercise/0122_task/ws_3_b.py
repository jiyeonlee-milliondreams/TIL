pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}


"""create_data 함수를 정의한다."""
def create_data(subject, day, title = None): # title 기본값 None 설정하기
    global pro_num # global에 정의된 pro_num을 함수 내에서 활용하기 위해 선언하기
    data = {'과목' : subject, '일차' : day, '제목' : title, '문제번호' : pro_num + 1}
    pro_num += 1
    return data


""" create_data 함수를 호출한다. """
result_1 = create_data('python', 3)

result_2 = create_data(day=1, subject='web', title='web 연습하기')

result_3 = create_data(**global_data) # 딕셔너리 중 값이 출력됨

print(result_1)
print(result_2)
print(result_3)


# result_3 = create_data(*global_data) # 딕셔너리 중 키가 출력됨
# print(result_3)
