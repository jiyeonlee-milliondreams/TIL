# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width # 가로
        self.height = height # 세로
    
    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'


shape1 = Shape(5, 3)
print(shape1)

'''
코드 설명
(1) 생성된 인스턴스에 클래스 자체에 인자를 두 개 받고 있으므로, __init__()에 인자를 두 개 설정한다. 
(2) __str__()은 인스턴스 변수를 받아와서 이를 문자열로 출력한다. 
    기본적으로 return이 존재한다.  
'''