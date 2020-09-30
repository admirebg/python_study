# -*- coding: utf-8 -*-

# decorator란
# 다른 함수의 인자로 원래 함수를 전달하여, 원래 함수의 수정없이 추가기능(전처리, 후처리)을 수행하도록 하는 구문


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


# def decorator_function(original_function):
#     print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
#     return original_function


@decorator_function
def display_1():
    print('display_1 실행')


@decorator_function
def display_2(arg1, arg2):
    print('display_2 실행 with {} {}'.format(arg1, arg2))


# display_1 = decorator_function(display_1)
# display_2 = decorator_function(display_2)


display_1()
display_2('a', 'b')



