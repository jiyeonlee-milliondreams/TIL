# https://www.acmicpc.net/problem/12927
# 위 링크에 들어가서 문제 풀어보세요! (공유 금지, 여러분들만 푸세요!)
# 문제를 꼭 직접 풀어보고, 어떤 식으로 풀어야하는 지 친구들끼리 공유하고, 논의하면서 꼭 경험해보세요!!!! 반드시 !!!!
    
arr = list(input())
N = len(arr)

# 전구 상태를 숫자로 변환: Y=1 (켜짐), N=0 (꺼짐)
switches = [1 if ch == 'Y' else 0 for ch in arr]
press_count = 0  # 스위치를 누른 횟수

# 1번 전구부터 N번 전구까지 차례대로 확인
for i in range(1, N + 1):
    # 현재 i번 전구가 켜져 있다면, i번 스위치를 누른다.
    if switches[i - 1] == 1:
        press_count += 1
        # i번 스위치는 i의 배수 번호를 가진 전구의 상태를 모두 반전시킨다.
        for k in range(i, N + 1):
            if k % i == 0:
                switches[k - 1] = 1 - switches[k - 1]

print(press_count)

# set으로 중복을 제거하고, 개수가 1개가 아니라면, -1 반환
# if len(set(switches)) == 1:
#     print(press_count)
# else:
#     print("-1")
