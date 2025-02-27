number_of_book = 100

def decrease_book(rental_once_number):
    print(f'남은 책의 수 : {number_of_book - rental_once_number}')

def rental_book(name, number):
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

rental_book('홍길동', 3)

