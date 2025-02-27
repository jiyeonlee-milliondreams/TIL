def solution(numbers, hand):
    answer = ''
    # 왼쪽 아래가 0,0
    left = [0, 0]
    right = [2, 0]
    for i in numbers:
        if i == 1:
            answer += 'L'
            left = [0, 3]
        elif i == 4:
            answer += 'L'
            left = [0, 2]
        elif i == 7:
            answer += 'L'
            left = [0, 1]
        elif i == 3:
            answer += 'R'
            right = [2, 3]
        elif i == 6:
            answer += 'R'
            right = [2, 2]
        elif i == 9:
            answer += 'R'
            right = [2, 1]
        elif i == 2:
            distance1 = abs(1 - left[0]) + abs(3 - left[1])
            distance2 = abs(1 - right[0]) + abs(3 - right[1])
            if distance1 < distance2:
                left = [1, 3]
                answer += 'L'
            elif distance2 < distance1:
                right = [1, 3]
                answer += 'R'
            else:
                if hand == "right":
                    right = [1, 3]
                    answer += 'R'
                else:
                    left = [1, 3]
                    answer += 'L'

        elif i == 5:
            distance1 = abs(1 - left[0]) + abs(2 - left[1])
            distance2 = abs(1 - right[0]) + abs(2 - right[1])
            if distance1 < distance2:
                left = [1, 2]
                answer += 'L'
            elif distance2 < distance1:
                right = [1, 2]
                answer += 'R'
            else:
                if hand == "right":
                    right = [1, 2]
                    answer += 'R'
                else:
                    left = [1, 2]
                    answer += 'L'
        elif i == 8:
            distance1 = abs(1 - left[0]) + abs(1 - left[1])
            distance2 = abs(1 - right[0]) + abs(1 - right[1])
            if distance1 < distance2:
                left = [1, 1]
                answer += 'L'
            elif distance2 < distance1:
                right = [1, 1]
                answer += 'R'
            else:
                if hand == "right":
                    right = [1, 1]
                    answer += 'R'
                else:
                    left = [1, 1]
                    answer += 'L'
        elif i == 0:
            distance1 = abs(1 - left[0]) + abs(0 - left[1])
            distance2 = abs(1 - right[0]) + abs(0 - right[1])
            if distance1 < distance2:
                left = [1, 0]
                answer += 'L'
            elif distance2 < distance1:
                right = [1, 0]
                answer += 'R'
            else:
                if hand == "right":
                    right = [1, 0]
                    answer += 'R'
                else:
                    left = [1, 0]
                    answer += 'L'

    return answer