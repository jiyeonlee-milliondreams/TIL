# import sys
# sys.stdin = open("palindrome_1_input.txt", "r")

# 회문 검사할 문자와 길이를 미리 설정
target = input()
n = len(target)

# 아래쪽 for가 문제없이 실행되면
# success는 여전히 True일 것이고
success = True
# 0 ~ n//2 까지 반복하며,
for i in range(n // 2):
    # 문자열의 i번째와 (n - 1 - i)번째를 비교한다.
    if target[i] != target[n - 1 - i]:
        # 회문이 아니다!
        # success는 False가 될거다.
        success = False
        # 한번 회문이 아니면 나머지 다 상관없이 회문이 아니다.
        break

if success:
    print(1)
else:
    print(0)
