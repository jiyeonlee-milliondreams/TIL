# 아래 클래스를 수정하시오.
class Person:
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name # 이름
        self.age = age # 나이
        Person.increase_number_of_people()   

    def introduce(self):
        print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')

    @classmethod
    def increase_number_of_people(cls):
        cls.number_of_people += 1


person1 = Person('Alice', 25)
# person2 = Person('jiyeon', 26) # 인스턴스가 생성될 때마다 증가하는지 확인하기 위해 작성.
person1.introduce()
print(Person.number_of_people)

'''
시행착오 일지
클래스 메서드를 정의하여 number_of_people 클래스 변수가 증가하도록 할 수 있으나, 
이는 [문제]의 요구사항인 "인스턴스가 생성될 때마다 증가하는 클래스 변수"가 아니라,
Person.increase_number_of_people()으로 해당 함수를 호출해야만 하는 것이므로 요구사항과 맞게끔 수정함.

# 초안
    @classmethod
    def increase_number_of_people(cls):
        cls.number_of_people += 1

Person.increase_number_of_people()
print(Person.number_of_people)

# 수정안
    def __init__(self, name, age):
        self.name = name # 이름
        self.age = age # 나이
        Person.number_of_people += 1

print(Person.number_of_people)

# 최종안
    def __init__(self, name, age):
        Person.increase_number_of_people()   

    @classmethod
    def increase_number_of_people(cls):
        cls.number_of_people += 1
        
'''
