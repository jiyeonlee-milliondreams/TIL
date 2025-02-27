# 모든 부분 집합을 생성하는 코드
arr = [1, 2, 3]
n = len(arr)  
subset_cnt = 2 ** n  # 생성 가능한 부분 집합의 총 개수

# 모든 부분 집합을 저장할 리스트
subsets = []  

# 생성할 수 있는 부분집합의 개수만큼 반복하면서 부분집합을 생성
for i in range(subset_cnt):  
    subset = []  # 현재 부분 집합을 저장할 리스트
    for j in range(n):  # 각 요소에 대해 포함 여부를 결정하기 위한 반복문 ( 주어진 리스트의 개수만큼)
        if i & (1 << j):  # i의 j번째 비트가 1인지 확인 ( 001, 010, 100 으로 계속 반복 )
            subset.append(arr[j])
    
    subsets.append(subset)

print(subsets)
