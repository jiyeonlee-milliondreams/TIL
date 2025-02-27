list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

'''
렌탈 리스트를 돌면서
렌탈책들이 리스트에 존재하는  확인하면 된다. 
존재하지 않으면 "가지고있지 않다" 출력 => 탈출한다.
탈출하지 않고, 모든 도서가 포함되어 있으면 대여가능 출력
'''

for rental_book in rental_list:
    if rental_book not in list_of_book:
        print(f'{rental_book} 은/는 보유하고 있지 않습니다.')
        break
else:
    print('모든 도서가 대여 가능한 상태입니다.')


''' 오류 일지 (1): for문을 중복으로 사용하여 결과값이 중복되어 출력됨. '''
# for rental_book in rental_list:
#     for library_book in list_of_book:
#         if rental_book == library_book:
#             print('모든 도서가 대여 가능한 상태입니다.')
#         else:
#             print(f'{rental_book}은/는 보유하고 있지 않습니다.')

''' 오류 일지 (2): for문을 탈출한다는 내용을 넣지 않아서 else가 또 출력됨.
    해결책: break를 넣어주면 됨. '''
# for rental_book in rental_list:
#     if rental_book in list_of_book:
#         pass
#     else:
#         print(f'{rental_book} 은/는 보유하고 있지 않습니다')
#         break
# else:
#     print('모든 도서가 대여 가능한 상태입니다.')

''' 오류 일지 (3): 결과가 아무것도 나오지 않음. '''
# for rental_book in rental_list:
#     if rental_book == list_of_book[0]:
#         pass
#     if rental_book == list_of_book[1]:
#         pass
#     if rental_book == list_of_book[2]:
#         pass
#     if rental_book == list_of_book[3]:
#         pass
#     if rental_book == list_of_book[4]:
#         pass
#     if rental_book == list_of_book[5]:
#         pass
#     if rental_book == list_of_book[6]:
#         pass
#     if rental_book == list_of_book[7]:
#         pass
#     if rental_book == list_of_book[8]:
#         pass
#     if rental_book == list_of_book[9]:
#         pass
#     if rental_book == list_of_book[10]:
#         pass
#     if rental_book == list_of_book[11]:
#         pass
#     if rental_book == list_of_book[12]:
#         pass
#     if rental_book == list_of_book[13]:
#         pass
#     else:
#         print(f'{rental_book}은/는 보유하고 있지 않습니다.')     
