class Stack:
    def __init__(self, capacity=10):
        # 초기 용량값 설정을 해주고, 용량에 맞춰서 리스트를 만들어야 한다.
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    # 스택이 가득찼는 지 확인하는 메서드
    def is_full(self):
        # 마지막을 가리치키는 top 포인터가 전체 용량의 -1 과 같으면 꽉 찬걸로 판단
        return self.top == self.capacity - 1
    
    def push(self, item):
        # 데이터를 집어넣기 전에 가득찼는 지부터 확인해야한다.
        if self.is_full():
            raise IndexError("Stack is full")
        # 데이터를 집어넣었으니 가장 마지막 원소를 가르키는 top 포인터 + 1
        self.top += 1
        # 그 포인터를 기준으로 데이터를 집어넣는다.
        self.items[self.top] = item

    # 스택이 비어있는 지 확인하는 메서드
    def is_empty(self):
        return self.top == -1

    # 가장 마지막 원소의 데이터를 꺼내는 메서드
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        # 데이터를 꺼내는 로직
        item = self.items[self.top]
        # 꺼낸거 초기화
        self.items[self.top] = None
        # top 포인터의 위치 한 칸 내린다.
        self.top -= 1
        # 꺼낸 데이터 반환한다.
        return item

    # 마지막 데이터를 조회하는 메서드
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        # top 포인터가 가리키는 마지막 원소를 조회!
        return self.items[self.top]

stack = Stack(3)

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1