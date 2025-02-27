import sys
sys.stdin = open("1989_input.txt", "r")

"""문자열 뒤집는 함수 정의"""
def reverse_txt(txt):
    N = len(txt)
    for i in range(N//2):   # 중간까지만 돌리면 전체 문자열이 뒤집어짐
        txt[i], txt[N-1-i] = txt[N-1-i], txt[i]     # 첫 문자열과 마지막 문자열 인덱스 손으로 써서 확인
        result = ''.join(txt)   # 문자열 공백 없이 반환
    return result

T = int(input())
for test_case in range(1, T+1):
    test_result = 0     # 회문이면 1, 회문이 아니라면 0
    txt = list(map(str, input().strip()))   # 문자열을 뒤집어서 자리를 바꾸려면 리스트로 저장

    join_txt = ''.join(txt)
    rev_txt = reverse_txt(txt)

    if join_txt == rev_txt:  # 원본 문자열과 뒤집어진 문자열 비교
        test_result += 1

    print(f'#{test_case} {test_result}')