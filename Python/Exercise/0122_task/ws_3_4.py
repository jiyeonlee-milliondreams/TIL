name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name, age, address):
    print(f'{name}님 환영합니다!')    
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    return user_info

# from 0122_task.python_ws_3_2.ws_3_2 import create_user

print(list(map(create_user, name, age, address)))