import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # swea 문제를 풀 때, 간혹 내 코드에 문제가 없는데
    # 안돌아가는 경우가 있어요
    word = input().strip()
    word_len = len(word)

    # 회문 검사 후 문제가 없다면 1을 반환하고, 문제가 있따면 0을 반환하죠
    # 검사를 하다가 회문이 아니면 0으로 바꾸고 출력
    result = 1

    # 회문 => 앞, 뒤 똑같은 전화번호? 문자열
    # 범위를 점점 좁혀가면서 비교를 할거죠. 그리고 이 범위는 문자열의 절반까지만 비교하면 됩니다.
    for idx in range(word_len // 2):
        # 서로 인덱스를 비교하고, 마주보면서 다가온다.
        # 값이 다르며 결과를 0으로 바꾸고 , 중단
        if word[idx] != word[word_len -1 - idx]:
            result = 0
            break

    print(f"#{test_case} {result}")