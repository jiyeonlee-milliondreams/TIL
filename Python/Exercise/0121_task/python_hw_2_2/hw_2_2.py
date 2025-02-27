book = '1'
total = 10
guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
print(guide)
print(len(list(book * total))) 

# print(type(book * total))을 활용해 Data Types 확인 결과 str이므로,
# 교안에 따라 str을 list로 변환하고 그 길이를 len으로 잼.

changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
rental = 3.0
print(changes)
print(int(total - rental))

# float을 int로 변환하여 문제 해결.
