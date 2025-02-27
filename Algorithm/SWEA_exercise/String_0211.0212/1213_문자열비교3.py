import sys
sys.stdin = open('1213_input.txt', 'rt', encoding='UTF8')

T = 10
for _ in range(1, T+1):
    test_case = int(input())
    word = input()
    sentence = input()

    m = len(word)
    n = len(sentence)

    count = 0

    i = 0
    while i <= n-m:
        # if 0 <= i + m < n:
        if sentence[i:i + m] == word:
            count += 1
            i += m
        else:
            i += 1
        # else:
        #     break
    print(f'#{test_case}', count)
