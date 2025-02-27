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