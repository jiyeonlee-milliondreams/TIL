# 1.
# 외계어를 전부 숫자로 바꾼 뒤,
# 숫자를 정렬한 다음,
# 숫자를 다시 외계어로 바꾸자.
alien_dict = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9,
}
numbers = input().split()
to_human = []
# 각각 외계어 숫자를 살펴보며 to_human에 더해주자.
for alien_number in numbers:
    to_human.append(alien_dict[alien_number])

to_human.sort()
alien_numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

result = []
# to_human의 각 값을 인덱스로 alien_numbers에서 가져온다.
for number in to_human:
    result.append(alien_numbers[number])
print(*result)

