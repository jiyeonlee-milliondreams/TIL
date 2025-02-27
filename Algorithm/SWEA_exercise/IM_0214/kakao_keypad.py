def solution(numbers, hand):
    left_hand = [3, 0]  # 왼손 초기값은 *의 이차원 배열상 위치
    right_hand = [3, 2]  # 오른손 초기값은 #의 이차원 배열상 위치

    temp_hand = [0, 0]  # 거리를 계산할 숫자 위치 임시 값

    result = ''  # 리턴할 결과
    for number in numbers:
        if number in [1, 4, 7]:
            result += 'L'
            left_hand = [number // 3, 0]
        elif number in [3, 6, 9]:
            result += 'R'
            right_hand = [number // 3 - 1, 2]
        else:  # 2, 5, 8, 0은 거리 계산 필요
            # 숫자 좌표 구하기
            if number in [0]:
                temp_hand = [3, 1]
            else:
                temp_hand = [number // 3, 1]

            # 왼손과 숫자 좌표, 오른손과 숫자 좌표의 거리 구하기
            left_hand_dist = abs(temp_hand[0] - left_hand[0]) + abs(temp_hand[1] - left_hand[1])
            right_hand_dist = abs(temp_hand[0] - right_hand[0]) + abs(temp_hand[1] - right_hand[1])

            # 거리에 따라 숫자 누를 손가락 결정
            if left_hand_dist > right_hand_dist:
                result += 'R'
                right_hand = [temp_hand[0], temp_hand[1]]
            elif left_hand_dist < right_hand_dist:
                result += 'L'
                left_hand = [temp_hand[0], temp_hand[1]]
            else:
                if hand == 'right':
                    result += 'R'
                    right_hand = [temp_hand[0], temp_hand[1]]
                elif hand == 'left':
                    result += 'L'
                    left_hand = [temp_hand[0], temp_hand[1]]
    return result


result = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")

print(result)
