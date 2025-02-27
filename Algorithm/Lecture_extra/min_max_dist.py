n = int(input())
numbers = list(map(int, input().split()))
# 일단, 최솟값 최댓값이 제일 앞에 있다고 가정하자.
min_value = numbers[0]
min_idx = 0
max_value = numbers[0]
max_idx = 0
# 1번째 숫자부터 검사하며,
for i in range(1, n):
    # 최솟값보다 작은지
    if numbers[i] < min_value:
        # 작으면 정보를 갱신한다.
        min_value = numbers[i]
        min_idx = i
    # 최댓값보다 큰지
    if numbers[i] >= max_value:
        # 크면 정보를 갱신한다.
        max_value = numbers[i]
        max_idx = i

# 일단, 서로 빼보자.
distance = max_idx - min_idx
# 만약 음수가 되면, 양수로 바꿔주자.
if distance < 0:
    distance *= -1
print(distance)

