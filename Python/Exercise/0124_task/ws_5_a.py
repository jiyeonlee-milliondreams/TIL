N = 9
data_1 = '123456789'
arr_1 = []
i = 0

for a in range(N):
    arr_1.append(data_1[i])
    i += 1

print(arr_1)


M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'

arr_2 = data_2.split(' ')
for odd in arr_2:
    if (int(odd) % 2) != 0:
        print(odd)
