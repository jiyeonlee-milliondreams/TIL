"""
input = abc

s1 = list(input())
s2 = input()

print(s1)   # ['a', 'b', 'c']
print(s1[1])    # b
print(s2)   # abc
print(s2[1])    # b
s1[1] = 'e'
print(s1)   # ['a', 'e', 'c']
# s2[1] = 'e'
# print(s2)     # abc 문자열은 불변.
s2 = 'aec'
print(s2)   # aec 재할당은 가능.
"""
"""
s = ['a', 'b', 'c']
print(*s)
print(''.join(s))
print('.'.join(s))
"""
""" 
문자열 뒤집기 
arr = list(input())
N = len(arr)
for i in range(N//2):   # 문자열 길이의 절반만 바꾸면 전체가 바뀌어서 나옴.
    arr[i], arr[N-1-i] = arr[N-1-i], arr[i]  # 조회한 arr[i]와 순열의 마지막 인덱스 N-1에서 i를 뺀 값 
print(arr)
"""
"""문자열 뒤집기 다른 방법"""
s = 'string'
s = s[::-1]  # 슬라이싱으로 뒤집기
print(s)    # gnirts
s_list = list(s)
s_list.reverse()    # 리스트로 형변환 후, 리스트 메서드 reverse() 활용하기.
print(s_list)   # ['s', 't', 'r', 'i', 'n', 'g']
print(''.join(s_list))  # string
