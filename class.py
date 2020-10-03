# -*- coding: utf-8 -*-


class Human():
    ''' 사람 '''

    def __init__(self, name, weight):   # 인스턴스 생성 시 실행됨
        ''' 초기화 함수 '''
        print('init 실행 {} {}'.format(name, weight))
        self.name = name
        self.weight = weight

    def __str__(self):  # 인스턴스를 출력할 때 사용되는 문자열 함수
        '''문자열화 함수'''
        return 'str 실행 {} {}'.format(self.name, self.weight)

    def eat(self):  # 메소드 : 클래스에 포함되어 있는 함수
        self.weight += 1
        print('weight {}'.format(self.weight))

    def say(self, message):
        print(message)


person1 = Human('ys', 50)
print(person1.name, person1.weight)
print(person1)

# person2 = Human()
#
# person1.language = 'korean'
# person1.weight = 50
#
# print(dir(person1))
# print(dir(person2))
#
# print(person1.language)
# print(person1.__doc__)
#
#
# def speak(person):
#     print('speak {}'.format(person.language))
#
#
# # speak(person1)
#
# Human.speak = speak
# person1.speak()
#
#
# # person 변수가 self로 전달됨. 즉 첫번째 인자에는 자동으로 self가 전달됨.
# person1.eat()
#
# person1.say('hi.')