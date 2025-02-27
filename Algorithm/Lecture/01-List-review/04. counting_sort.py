# 필독!!!
# 알고리즘 구현 코드에 정답은 없습니다!!!!!
# 구현은 다양한 방식으로 할 수 있으며, 더 효율적인 방법이 존재할 수 있습니다.
# 각 알고리즘의 핵심 개념만 구현되어 있다면, 모두 훌륭한 코드입니다. 
# 따라서 아래 코드를 참고하여, 본인만의 방식으로 해당 알고리즘을 구현해보기를 권장합니다.

def counting_sort(arr, max_value):
    n = len(arr)  # 배열의 길이
    # 각 숫자마다 나오는 개수를 저장하는 배열을 만들어야죠.
    # 배열안에 있는 값 중에서 최대값의 + 1 만큼 0을 할당해야 한다.
    count_arr = [0] * (max_value + 1)  # 요건 0이 개수를 의미하는 거니까, 반드시 0 이여야하고
    result = [0] * n  # 여기에서 0 은 아무렇게나 해도 된다. 그냥 빈 값을 의미하는 것임

    # 1. 각 요소가 몇 번 나왔는 지 확인해야 한다.
    for num in arr:
        count_arr[num] += 1

    # 2. 누적합 배열을 만들어야 한다.
    for i in range(1, len(count_arr)):
        # 이전까지 나온 수들의 합을 누적하는 코드
        count_arr[i] += count_arr[i-1]

    # 3. 거꾸로 순회하면서 (기존에 주어진 배열에서 )
    # 누적합 배열에서 자신이 놓여야 할 위치를 찾아간다. (안정성 확보를 위해서)
    for i in range(n-1, -1, -1):    # 왜냐면 미포함이니까 ( -1까지)
        val = arr[i]
        # count_arr => 누적합 배열에서 현재 값이 들어가야하는 위치에 저장한다.
        result[count_arr[val] - 1] = val
        # count_arr[val] = count_arr[val] - 1
        count_arr[val] -= 1

    return result

arr = [0, 4, 1, 3, 1, 2, 4, 1]
result = counting_sort(arr, 4)
print(result)  # [0, 1, 1, 1, 2, 3, 4, 4]