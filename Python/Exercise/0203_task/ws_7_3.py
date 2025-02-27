# 아래 클래스를 수정하시오.
class Shape:
    
    def __init__(self, width, height):
        self.width = width # 가로
        self.height = height # 세로
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height) # 둘레 = 2 * (가로 + 세로)


shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
