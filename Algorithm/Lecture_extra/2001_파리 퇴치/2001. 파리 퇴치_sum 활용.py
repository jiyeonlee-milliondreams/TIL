"""
이 코드의 요지는 이전 코드와 차이가 없다는 것이다.
즉, sum이나 max를 사용하는 것도 for loop => O(N)의 시간복잡도를 갖는다는 것이다. 
"""
import sys
sys.stdin = open("input.txt", "r")

T = int(input().strip())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    kill_flies = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # grid[i:i+M]는 M개의 행, 각 행의 j부터 j+M까지의 슬라이스의 합을 구함
            tmp_sum = sum(sum(row[j:j+M]) for row in grid[i:i+M])
            kill_flies = max(kill_flies, tmp_sum)
            
    print(f"#{test_case} {kill_flies}")
