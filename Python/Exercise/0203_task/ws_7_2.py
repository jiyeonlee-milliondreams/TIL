# 아래 클래스를 수정하시오.
class Shape:

    def __init__(self, width, height):
        self.width = width # 가로
        self.height = height # 세로

    def calculate_area(self):
        return self.width * self.height # 넓이 = 가로 * 세로

shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)


'''
시행착오 일지
인스턴스 메서드 작성시, 첫 인자로 반드시 self를 넣어야 함. 

(초안)
    def calculate_area():
        return self.width * self.height # 넓이 = 가로 * 세로

TypeError: calculate_area() takes 0 positional arguments but 1 was given

(수정안)
    def calculate_area(self):
        return self.width * self.height # 넓이 = 가로 * 세로    
'''