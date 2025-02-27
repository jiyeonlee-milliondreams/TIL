"""A와 B의 글자를 차례로 늘어놓기"""
A = 'abcd'
B = 'efghijklmn'

'''
문자열인 경우
N = len(A)
M = len(B)
i = j = 0
ans = ''
while i+j < N+M:    # 복사할 문자가 남아있으면
    if i < N:   # A에 남은 문자가 있으면
        ans += A[i]
        i += 1
    if j < M:
        ans += B[j]
        j += 1
print(ans)
'''

'''리스트인 경우'''
N = len(A)
M = len(B)
i = j = 0
ans = [0] * (N+M)
while i+j < N+M:
    if i < N:
        ans[i+j] = A[i]
        i += 1
    if j < M:
        ans[i+j] = B[j]
        j += 1
print(''.join(ans))