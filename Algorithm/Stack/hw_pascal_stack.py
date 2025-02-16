N = int(input())

prev_stack = [1]

for i in range(1, N):
    new_stack = [1]

    for j in range(len(prev_stack) - 1):
        new_stack.append(prev_stack[i-1][j-1] + prev_stack[i-1][j])

    new_stack.append(1)

    prev_stack = new_stack
