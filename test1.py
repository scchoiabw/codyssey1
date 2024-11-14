class Person:
    def __init__(self, name, age):  # 생성자
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# 객체 생성
person1 = Person("Alice", 25)
print(person1.greet())
