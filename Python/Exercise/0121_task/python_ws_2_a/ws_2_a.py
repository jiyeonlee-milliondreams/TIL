# zero_list
zero_list = [0]
print(zero_list)

# many_zero_list
many_zero_list = [0] * 250000
# [[0] * 250000] 인 경우, [0]이라는 리스트를 250000번 반복하지만, 왜 안될까?
print(len(many_zero_list))

# numbers
numbers = list(range(1,11))
print(numbers)
print(numbers[3:])
