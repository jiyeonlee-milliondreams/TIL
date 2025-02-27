# https://www.acmicpc.net/problem/12927

'''완전탐색으로 풀기 어려우므로 탐욕 알고리즘 배운 후 다시 도전!!'''

arr = list(input())
N = len(arr)
off = []

for i in range(N):  # 불이 꺼진 곳의 인덱스 + 1 구하기.
    if arr[i] == 'N':
        off.append(i+1)


switch = -1  # 초기값 1
if len(off) == N:
    switch = 0
else:   # 최종적으로 모든 스위치가 Y로 켜진 상황에서 N으로 바꾸기 위해 '첫번째' 스위치를 켤 것이므로 1 더하기
    switch += 2
    while 0 < len(off) < 1000:     # off 길이가 0과 같아지면  while 문 종료
        min_off = min(off)
        for a in range(min_off, N+1, min_off):    # 불이 꺼진 곳의 인덱스 +1 중 최소값의 배수 만들기 하나씩 호출
            for i in range(len(off)):    # off 길이만큼 반복
                if a == off[i]:
                    off.pop(i)
                    break   # 일치하면 다음으로
            else:   # for 문 돌고 없으면 해당 배수 추가.
                off.append(a)
        switch += 1

print(switch)


# switches = [1 if ch == 'Y' else 0 for ch in arr]
# for switch in switches:
#     if switches == 0:
#         print("-1")
#         break
# else:
#     print(switch)
#
# i_double(10, 2)
# if  # 모든 전구 끌 수 없다면?
#
# print(switch)
#
# switches = [1 if ch == 'Y' else 0 for ch in arr]
# for switch in switches:
#     if switch == 0:
#         print("-1")
#         break
