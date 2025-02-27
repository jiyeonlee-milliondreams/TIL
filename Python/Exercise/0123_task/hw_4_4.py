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

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


missing_book = [book_1 for book_1 in rental_book if book_1 not in list_of_book]

for book_2 in missing_book:
    print(f'{book_2} 을/를 보충하여야 합니다.')

if len(missing_book) <= 0:
    print('모든 도서가 대여 가능한 상태입니다.')

''' for else 활용하기보다 조건문을 추가해서 "보충하여야 합니다"와 "대여 가능한 상태"가 중복적으로 나오는 문제 해결'''
# else:
#     print('모든 도서가 대여 가능한 상태입니다.')

'''리스트 컴프리헨션 사용 전'''
# missing_book = []

# for book in rental_book:
#     if book not in list_of_book:
#         missing_book.append(book)
#         print(f'{book}을 보충하여야 합니다.')
#         if len(missing_book) >= 3:
#             break
# else:
#     print('모든 도서가 대여 가능한 상태입니다.')

'''리스트 컴프리헨션 사용 후'''
# missing_book = [book_1 for book_1 in rental_book if book_1 not in list_of_book]

# for book_2 in missing_book:
#     print(f'{book_2} 을/를 보충하여야 합니다.')

# else:
#     print('모든 도서가 대여 가능한 상태입니다.')


