import sys

sys.stdin = open('input.txt')

# 처음과 끝이 다르면, 바로 return False로 인해서 속도가 훨씬 빠르다.
def is_palindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

# 문자열이 회문인지 확인하는 함수
# 뭐가 됐든 무조건 뒤집어야하니까 속도가 좀 느리다.
def is_palindrome_simple(string):
    return string == string[::-1]


# 가장 긴 회문을 찾는 함수
def find_longest_palindrome(matrix):
    max_length = 1  # 가장 긴 회문의 글자 수를 저장할 변수

    # 긴 길이부터 검사를 할거다! ( 100, 99, 98, ..., 2 )
    for length in range(N, 1, -1):  # 100개짜리 회문이 있는지를 먼저 검사한다. # 다음에는 99로 바뀌겠죠.
        # 행을 하나 잡고서, 그 행에 있는 회문을 찾자 ( 0, , ... 100 )
        for i in range(N):  # i =0 => 1행 잡아두고
            for start in range(N - length + 1):  # 해당 행에서 주어진 회문 길이를 몇번 실행하냐에요
                if is_palindrome_simple(matrix[i][start: start + length]):
                    # 회문을 찾았으면 해당 길이를 바로 반환시킴 ( 왜냐면 가장 긴 것부터 찾았으니까)
                    return length

                column = []
                # i 열을 고정해놓고, [start: start+length] 잘라서 열별로 접근해서 하나의 리스트에 담는다.
                for j in range(start, start + length):
                    column.append(matrix[j][i])

                # 열을 담은 리스트를 대상으로 회문검사한다.
                if is_palindrome_simple(column):
                    return length

    return max_length


for test_case in range(1, 11):
    tc = int(input())
    N = 100
    matrix = [input() for _ in range(N)]

    result = find_longest_palindrome(matrix)
    print(f"#{tc} {result}")
