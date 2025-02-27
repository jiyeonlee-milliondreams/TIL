n = int(input())
# 0과 1로 이루어진 **문자열**이다.
nums = input()

# 최대 길이를 기록할 변수를 만든다.
max_length = 0
# 그다음 확인할 위치를 기록할 변수를 만든다.
idx = 0
# idx < n일 동안 (nums를 다 확인할 동안)
while idx < n:
    # 만약 1이 시작되면 그 길이가 얼마인지 저장할 변수를 만든다.
    length = 0
    # idx가 nums의 범위를 벗어나지 않을 동안 +
    # nums[idx] == '1'일 동안 반복해서 횟수를 센다
    while idx < n and nums[idx] == '1':
        # 그때마다 위치를 이동하고 길이를 증가시킨다.
        length += 1
        idx += 1
    # 만약 이번 1의 길이가 더 길었다면 갱신한다.
    max_length = max(max_length, length)
    idx += 1

print(max_length)
