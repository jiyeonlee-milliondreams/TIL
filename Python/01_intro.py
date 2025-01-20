# python_ws_1_4

# 원주율
ratio = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
redius = 15
# 원의 둘레
circumference = redius * 2 * ratio
# 원의 넓이
extent = redius ** 2 * ratio

reply_ratio = '원주율 : '
reply_redius = '반지름 : '
reply_circumference = '원의 둘레 : '
reply_extent = '원의 넓이 : '


print(f'{reply_ratio} {ratio}')
print(f'{reply_redius} {redius}')
print(f'{reply_circumference} {circumference}')
print(f'{reply_extent} {extent}')

# python_ws_1_5

a = 3*2
b = 3**2
c = (-3)**2

print(a)
print(b)
print(b//a, b%a)
print(b + c)


# python_ws_1_b

# korean 변수에 '한글' 문자열을 할당한다.
korean = '한글' 

# english 변수에 'english' 문자열을 할당한다.
english = 'english'

# number 변수에 3정수를 할당한다.
number = 3

# 각 변수에 담긴 값을 출력한다.
# print(korean)
# print(english)
# print(number)

# f-string을 활용하여 '한글과 english'문자열을 출력한다.
    # 단, korean과 english 변수를 사용하여야 한다.
print(f'{korean}과 {english}')

#korean 변수를 number만큼 곱한 결과를 출력한다. 
print(korean * number)
