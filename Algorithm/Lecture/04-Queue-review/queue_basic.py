# 선형 큐
'''

장점: 직관적
단점: front와 rear를 오른쪽으로 한 칸 씩 옮겨가며 삽입, 삭제를 하기 때문에
    포화상태로 인식되어 앞에 남아있는 빈 공간을 잘 확용하지 못함.
해결책: 배열의 처음과 끝이 연결되어있다고 논리적으로 생각하는 원형 큐 활용

'''
# 큐 생성
queue = [0] * 3
front = rear = -1  # 초기상태는 front, rear 모두 -1

# 1, 2, 3을 인큐하기
rear += 1  # enqueue 1
queue[rear] = 1

rear += 1  # enqueue 2
queue[rear] = 2

rear += 1  # enqueue 3
queue[rear] = 3

# 디큐하기   front 1 증가 후 새로운 리스트에 저장하거나 연산에 활용할 수 있음. 여기서는 출력만 해서 확인.
front += 1
print(queue[front])  # 1

front += 1
print(queue[front])  # 2

front += 1
print(queue[front])  # 3

# 문제에서 디큐를 하면서 일처리를 하는 방법
while front != rear:  # 큐에 원소가 남아있으면
    front += 1
    t = queue[front]

# 큐를 활용하는 간단한 방법
q = []
q.append(1)  # enqueue
q.append(2)
q.append(3)
print(q.pop(0))  # dequeue   pop(0)dms 맨 앞 원소만 출력
print(q.pop(0))
print(q.pop(0))


# 원형 큐
'''

구조: front는 비워둔 채 진행. 나머지 연산 mod 활용.
공백상태:
포화상태:

'''

# 연결 리스트를 활용한 큐


