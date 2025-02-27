import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users/'
response = requests.get(API_URL)
parsed_data = response.json()
list(parsed_data)

dummy_data = []

for user_info in parsed_data:
    dummy_data.append(user_info['name'])

print(dummy_data)


# # 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/'

# # API 요청
# response = requests.get(API_URL)

# # JSON -> dict 데이터 변환
# parsed_data = response.json()

# # dict -> list 형변환
# # 목적: parsed_data에 순서를 부여하기 위해
# list(parsed_data)

# # dummy_data를 비어있는 리스트로 정의
# dummy_data = []

# # 반복문을 사용하여 1부터 10까지 10명의 데이터 요청.
# # print(parsed_data)를 해보니 데이터가 10개여서 range 없이 반복문 활용.
# # dummy_data에 응답받은 사용자의 name을 리스트에 추가.
# for user_info in parsed_data:
#     dummy_data.append(user_info['name'])

# # 예시화면과 같이 dummy_data 출력.
# print(dummy_data)

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
