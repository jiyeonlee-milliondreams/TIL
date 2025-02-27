'''
0<=DATA[i]<=4 # 주어진 조건
'''

DATA = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(DATA)

Counts = [0] * 5 # max(DATA) + 1, 크기에 주의!

Temp = [0] * N

'''
아래와 같이 하면 오류
# N = len(DATA)
# Counts = [0] * N
'''

# 암기!
for i in range(N):          # 각 숫자의 개수
    Counts[DATA[i]] += 1

for i in range(1, 5):       # Counts[i]까지의 합계
    Counts[i] += Counts[i-1]

for i in range(N-1, -1, -1):
    Counts[DATA[i]] -= 1 # DATA[i]까지의 개수 1개 감소
    # DATA[i]까지 차지한 칸 수 중 가장 오른쪽에 DATA[i] 기록
    Temp[Counts[DATA[i]]] = DATA[i]

print(Temp)

# K가 인덱스로 읽을 수 있는 경우에만 활용 가능.