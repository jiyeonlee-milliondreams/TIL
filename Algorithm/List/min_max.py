n = int(input())
numbers = list(map(int, input().split()))

# 일단 최소값과 최대값이 제일 앞에 있다고 가정
min_value = numbers[0]
min_idx = 0
max_value = numbers[0]
max_idx = 0

# 1번째 숫자부터 검사
for i in range(1, n):
    # 최소값보다 작은 경우에 갱신하면 앞 인덱스가 저장됨.
    if min_value > numbers[i]:
        min_value = numbers[i]
        min_idx = i
    # 최대값이 같거나 큰 경우에 갱신해야 뒤 인덱스가 저장됨.
    if max_value <= numbers[i]:
        max_value = numbers[i]
        max_idx = i

# 일단 서로 빼보자.
distance = max_idx - min_idx
if distance < 0:
    distance = -distance

print(distance)
        