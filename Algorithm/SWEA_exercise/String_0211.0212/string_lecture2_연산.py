a1 = '123456789'
a2 = '123456788'
print(a1 == a2)

"""
==  # 내용의 동일성 검증. 같은 모양인가?
is  # 메모리 주소의 동일성 검증. 같은 메모리 위치인가?
"""

s1 = 'abc'
s2 = 'ab'
s3 = s2 + 'c'
print(s1, s3)
print(s1 == s3)
print(s1 is s3)

"""문자열 간 비교"""
s1 = 'ab'
s2 = 'ab'
s3 = 'ac'
s4 = 'AC'
s5 = 'abc'
print(s1 == s2)  # True
print(s1 < s2)  # False
print(s1 < s3)  # 알파벳 순서상 c가 나중에 있으므로 True
print(ord('a'), ord('A'))   # 97 65
print(s3 < s4)  # 유니코드 기준 대문자의 코드가 더 숫자가 적으므로 False
print(s1 < s5)  # 글이 더 많으면 True

"""진수 변환 - 계산기 프로그래머 ver 활용"""
a = 'A'
b = int(a, 16)  # A를 16진수로 표현하면 10
print(b)

c = '1001'
d = int(c, 2)   # 1001을 2진수로 표현하면 9
print(d)
