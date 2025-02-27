# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width # 가로
        self.height = height # 세로
        
    def print_info(self):
        Area = self.width * self.height # 넓이 = 가로 * 세로
        Perimeter = 2 * (self.width + self.height) # 둘레 = 2 * (가로 + 세로)
        print(f'Width: {self.width}\nHeight: {self.height}\nArea: {Area}\nPerimeter: {Perimeter}')
        # f-string을 활용하여 줄바꿈을 포함하여 출력


shape1 = Shape(5, 3)
shape1.print_info()

'''
시행착오 일지
print_info() 인스턴스 메서드를 return으로 반환하니, 메서드를 호출한 후에 출력의 과정도 거쳐야 함.
[문제] 요구사항은 "메서드를 추가하여 가로, 세로, 넓이 둘레를 출력하시오"라고 되어있으므로, 메서드 자체를 print()로 수정함.
덧붙여, clone받은 초기 .py 파일도 메서드를 호출만 하여 출력되게끔 하고 있으므로, 메서드 자체가 출력이 되어야 함. 
(초안)
    def print_info(self):
        Area = self.width * self.height
        Perimeter = 2 * (self.width + self.height)
        return f'Width: {self.width}\nHeight: {self.height}\nArea: {Area}\nPerimeter: {Perimeter}'


shape1 = Shape(5, 3)
shape1.print_info()
print(shape1.print_info())

(수정안)
    def print_info(self):
        Area = self.width * self.height
        Perimeter = 2 * (self.width + self.height)
        print(f'Width: {self.width}\nHeight: {self.height}\nArea: {Area}\nPerimeter: {Perimeter}')



shape1 = Shape(5, 3)
shape1.print_info()
'''