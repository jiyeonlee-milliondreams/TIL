""" 방법(1) 
전역 변수를 함수 내에서 활용하고 싶을 때, global 키워드 사용"""

number_of_people = 0


def increase_user():
    global number_of_people 
    number_of_people += 1
    print(f'현재 가입된 유저 수: {number_of_people}') 

increase_user()

# 실행 결과 값과 동일하게 출력하기 위해 f-string을 활용한다.


""" 방법 (2)
함수 내에서만 정의하기"""

"""
def increase_user():
    number_of_people = 0 
    number_of_people += 1

increase_user()
print(number_of_people)
"""