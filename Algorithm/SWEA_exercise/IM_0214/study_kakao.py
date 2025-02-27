phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [100, 0, 200]]

numbers = list(map(int, input()))
numbers

print(numbers)

def solution(numbers, hand):
    l = [3, 0]  # * 좌표.
    r = [3, 2]  # # 좌표.

    ans = ''
    for num in numbers:
        # 1, 4, 7은 왼손 이동.
        if num in [1, 4, 7]:
            ans += 'L'
            l = [num//3, 0]
        # 3, 6, 9는 왼손 이동.
        elif num in [3, 6, 9]:
            ans += 'R'
            r = [num//3 - 1, 2]
        else:
            # 0의 좌표.
            if num == 0:
                n = [3, 1]
            # 2, 5, 8의 좌표.
            else:
                n = [num//3, 1]

            # 이동해야 할 거리.
            move_l = abs(l[0] - n[0]) + abs(l[1] - n[1])
            move_r = abs(r[0] - n[0]) + abs(r[1] - n[1])

            # 왼손 거리가 더 가깝거나 거리는 같지만 왼손잡이인 경우.
            if move_l < move_r or (move_l == move_r and hand == 'left'):
                l = n
                ans += 'L'

            # 오른손 거리가 더 가깝거나 거리는 같지만 오른손잡이인 경우.
            elif move_l > move_r or (move_l == move_r and hand == 'right'):
                r = n
                ans += 'R'

    return ans

