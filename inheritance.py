# -*- coding: utf-8 -*-


class Animal():

    def __init__(self):
        print('animal init')

    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("인사한다")


class Human(Animal):    # 상속

    def __init__(self):
        print('human init')

    def wave(self):
        print("손을 흔든다")


class Dog(Animal):      # 상속
    def wag(self):
        print("꼬리를 흔든다")

    def greet(self):    # 오버라이드
        self.wag()
        super().greet() # 부모 클래스의 함수 실행


animal = Animal()
animal.walk()

person = Human()
person.walk()
person.eat()
person.wave()
person.greet()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()
dog.greet()
