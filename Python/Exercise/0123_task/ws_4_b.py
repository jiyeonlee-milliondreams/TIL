food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

''' for문 코드 '''
for food in food_list:
    if food['이름'] == '토마토':
        food['종류'] = '과일'
    if food['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    print(f'{food["이름"]} 은/는 {food["종류"]} (이)다.')
    # print(f'({food["이름"]} 은/는 {food['종류']} (이)다.)')
    # 작은 따옴표는 왜 안될까? 작은 따옴표를 중복해서 작성해서 이를 하나의 f-string으로 인식하기 때문.

print(food_list)

''' while문 코드 '''

# bash = False

contents = food_list[0]['이름']
print(contents)

while food_list:
    print(f'{food["이름"]} 은/는 {food["종류"]} (이)다.')


