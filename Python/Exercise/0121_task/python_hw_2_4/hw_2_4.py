# 방법 (1) authors의 data types을 기존 list에서 set으로 바꿔서 중복을 제거한 후,
#          다시 list로 형변환을 해서 출력한다. 

authors = {
    '작자 미상',
    '이항복',
    '임제',
    '임제',
    '조성기',
    '조성기',
    '조성기',
    '임제',
    '허균',
    '허균',
    '허균',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '임제',
    '박지원',
    '이항복',
    '남영로',
    '남영로',
    '남영로',
    '이항복',
    '임제',
    '임제',
}

print(list(authors))

# 방법 (2) authors의 data types을 기존 list을 유지한 채로 set으로 형변환해서 중복을 제거한 후,
#         다시 list로 형변환을 해서 출력한다. 

# authors = [
#     '작자 미상',
#     '이항복',
#     '임제',
#     '임제',
#     '조성기',
#     '조성기',
#     '조성기',
#     '임제',
#     '허균',
#     '허균',
#     '허균',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '박지원',
#     '이항복',
#     '남영로',
#     '남영로',
#     '남영로',
#     '이항복',
#     '임제',
#     '임제',
# ]

# print(list(set(authors)))

