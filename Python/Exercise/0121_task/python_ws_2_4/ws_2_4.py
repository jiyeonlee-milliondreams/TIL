information_1 = dict()
information_2 = dict()
information_3 = dict()
information_4 = dict()
information_5 = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

# info_list = []
# info_list.append({123})
# print(info_list)

information_1[authors[0]] = books[1]
information_2[authors[1]] = books[3]
information_3[authors[2]] = books[4]
information_4[authors[3]] = books[0]
information_5[authors[4]] = books[2]

# print(f'{information_1}\n{information_2}\n{information_3}\n{information_4}\n{information_5}')
# print(information_1)
# print(information_2)
# print(information_3)
# print(information_4)
# print(information_5)
# print(information_5.keys())
# print(information_5.values())
# print(information_5.items())

print(f'{list(information_1.keys())[0]} : {list(information_1.values())[0]}')
print(f'{list(information_2.keys())[0]} : {list(information_2.values())[0]}')
print(f'{list(information_3.keys())[0]} : {list(information_3.values())[0]}')
print(f'{list(information_4.keys())[0]} : {list(information_4.values())[0]}')
print(f'{list(information_5.keys())[0]} : {list(information_5.values())[0]}')



# information = dict()
# authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
# books = [
#     ['장화홍련전', '가락국 신화', '온달 설화'],
#     ['금오신화', '이생규장전', '만복자서포기'],
#     ['수성지', '백호집', '원생몽유록'],
#     ['홍길동전', '장생전', '도문대작'],
#     ['옥루몽', '옥련몽'],
# ]

# information[authors[0]] = books[1]
# information[authors[1]] = books[3]
# information[authors[2]] = books[4]
# information[authors[3]] = books[0]
# information[authors[4]] = books[2]

# print(information)
