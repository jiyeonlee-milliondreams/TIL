title = '딕셔너리 활용하기'

# 딕셔너리 할당하기
data = {'과목': 'Python', '구분': '실습', '단계': 2, '문제번호': 3251, '이름': None, '일차': 22}
print(data)

# 딕셔너리 변경 연습하기
data['단계'] = str(data['단계']) + '단계'
data['이름'] = title
data['일차'] -= 20
print(data)