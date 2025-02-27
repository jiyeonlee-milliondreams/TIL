# 첫번째 input()은 세고 싶은 글자들
letters = input()
# 두번째 input()은 몇개가 있는지 셀 대상
source = input()
# 각 글자가 몇번 등장했는지 세는 dict를 만들자.
count_dict = {}
# letters가 가지고 있는 글자들을 세고 싶으니,
# 그 글자를 count_dict의 key로 넣어주자.
for letter in letters:
    count_dict[letter] = 0
    print(count_dict)

# source의 글자를 확인하면서,
for char in source:
    # 글자가 count_dict에 있으면
    if char in count_dict:
        # 하나 증가시켜준다.
        count_dict[char] += 1

# count_dict에서 가장 큰 value를 찾는다.
max_count = 0
"""
for key in count_dict:
    print(key)
print()
for key in count_dict.keys():
    print(key)
print()
for value in count_dict.values():
    print(value)
"""

for value in count_dict.values():
    if value > max_count:
        max_count = value

print(max_count)
