a = 2, 3, 7
# bit = [0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             # s = 0     # 부분집합의 합
#             for b in range(3):
#                 if bit[b]:
#                     print(a[b], end=' ')  # 부분집합의 원소
#                     # s += a[b]
#             print()

'''비트 연산자를 활용한 부분집합 구하기'''
# 코드를 보고 이해할 수 있으면 충분.
# 4837. 부분집합의 합
#
# A = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
# n = len(A)
#
# for i in range(1<<n):   # 부분집합의 개수
#     for j in range(n):  # 원소의 수만큼 비트를 비교
#         if 1&(1<<j):    # i의 j번 비트가 0이 아닌 경우
#             print([arr[j]], end=',')
#     print()
# print()
#
# T = int(input())
# N, K = map(int, input().split())


bit = []
for i in range(12*2*3):  # N 부분집합의 개수
    bit.append(i)
print(2**12)