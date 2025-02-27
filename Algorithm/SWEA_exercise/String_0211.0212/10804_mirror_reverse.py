import sys

sys.stdin = open("10804_input.txt", "r")

T = int(input())

mirror_dict = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

for test_case in range(1, T + 1):

    origin_str = list(map(str, input()))
    N = len(origin_str)

    # 문자열 뒤집기는 문자열을 2로 나눈 몫만큼만 진행.
    for i in range(N // 2):
        # 가운데를 기준으로 같은 거리만큼 떨어진 값을 교환
        origin_str[i], origin_str[N - 1 - i] = origin_str[N - 1 - i], origin_str[i]

    for i in range(N):
        for key in mirror_dict:
            if origin_str[i] == key:
                origin_str[i] = mirror_dict[key]
                # 만약 original_str[i]와 key가 동일하여 변환을 했다면 더 이상의 변환 없이 반복 종료
                # 다음 i로 넘어가게 됨.
                break

    print(f'#{test_case}', ''.join(origin_str))

    # if char == mirror_dict[char]:
    #     char =

    # mirror_dict의 key와 origin_str[i]가 일치하면 value로 변환
    # for i in range(N):
    #     if origin_str[i] == mirror_dict:
    #         origin_str[i] = mirror_dict[origin_str[i]]
    #
    # print(origin_str)

    # for char in origin_str:
    #     if char == mirror_dict:
    #         char = mirror_dict[char]
