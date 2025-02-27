number_of_people = 0

# from python_ws_3_1 import ws_3_1

def increase_user():
    global number_of_people 
    number_of_people += 1
    print(f'현재 가입된 유저 수: {number_of_people}')

# increase_user()
# print(f'현재 가입된 유저 수: {number_of_people}') 


def create_user(name, age, address):
    print(f'{name}님 환영합니다!')    
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    return user_info




user_info = {'name': '홍길동', 'age': 30, 'address': '서울'}
result = create_user(**user_info)
print(result)

