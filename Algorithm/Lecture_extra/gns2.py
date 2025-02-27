
# 2.
# 외계어가 각각 몇번 등장했는지 센 다음
# ZRO부터 몇번씩 등장했느냐에 따라 출력을 바꿔준다.
# Counting Sort랑 유사하지만 다름!
alien_numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
count_dict = {
    'ZRO': 0,
    'ONE': 0,
    'TWO': 0,
    'THR': 0,
    'FOR': 0,
    'FIV': 0,
    'SIX': 0,
    'SVN': 0,
    'EGT': 0,
    'NIN': 0,
}
# 외계어를 받아오고,
numbers = input().split()
# 각 숫자를 key로 가진 count_dict의 value을 올려준다.
for number in numbers:
    count_dict[number] += 1
# 그럼 count_dict의 각 숫자의 등장 횟수가 기록된다.

result = []
# 순서 유지를 위해 alien_numbers를 순회하며,
for alien_number in alien_numbers:
    # count_dict에 저장된 alien_number의 등장 횟수만큼
    for _ in range(count_dict[alien_number]):
        # result에 alien_number를 넣어준다.
        result.append(alien_number)

print(' '.join(result))
