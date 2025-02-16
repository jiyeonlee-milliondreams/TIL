T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # 파스칼 행의 길이

    pascal = [[1]]
    i = 1   # 0번 인덱스의 행을 1로 미리 채워뒀으므로 i = 1부터 시작

    while i < N:    # i = N-1까지 반복하며 pascal 행 추가
        row = [1]  # pascal에 추가할 행을 빈 리스트 row로 생성. 행이 변화할 때마다 초기화
        j = 1       # 첫 열은 1이므로 1번 인덱스부터 반복
        while j <= i - 1:    # 열이 i-1까지 반복
            row[j] = pascal[i-1][j-1] + pascal[i-1][j]      # 파스칼 왼쪽 위, 바로 위 인덱스의 값 더해서 받기

        row.append(1)   # 반복을 돌고나서 row 마지막에 1 추가
        pascal.append(row)  # 완성된 열을 pascal에 추가

        i + 1

    print(f'#{test_case}', pascal)