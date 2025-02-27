import sys
sys.stdin = open("input.txt", "r")

# 함수에 들어갈 변수,
# 범위를 줄이거나, 종료조건을 검사하기 위한 변수가 들어갑니다.
def is_palindrome(word, left, right):
    # 종료 조건
    # left >= right 경우, 서로 비교가 다 끝났기 때문에 재귀를 종료한다.
    if left >= right:
        return True

    if word[left] != word[right]:
        return False

    return is_palindrome(word, left + 1, right - 1)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word = input().strip()
    word_len = len(word)
    result = is_palindrome(word, 0, word_len - 1)
    print(f"#{test_case} {int(result)}")
