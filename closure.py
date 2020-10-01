# -*- coding: utf-8 -*-

# 클로저란
# 퍼스트클래스 함수를 지원하는 언어의 네임 바인딩 기술이다.

def outer_func():
    message = 'hi'

    def inner_func():
        print(message)

    return inner_func       #함수의 오브젝트를 리턴

my_func = outer_func()

print(my_func)
print(dir(my_func))
print(type(my_func.__closure__))
print(my_func.__closure__)
print(my_func.__closure__[0])
print(dir(my_func.__closure__[0]))
print(my_func.__closure__[0].cell_contents)


# 프리변수란 그 함수 안에서 사용되었지만 정의는 되지 않은 변수를 말함. 위 예시에서는 message 변수임.
# 클로저는 함수의 프리변수 값을 __closure__에 저장한다

