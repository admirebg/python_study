# -*- coding: utf-8 -*-

#  python 프로그래밍 언어는 함수를 first-class function으로 지원한다.
# 퍼스트 클래스 함수란, 함수를 변수에 할당할 수 있으며, 다른 함수의 인자로 전달하거나 함수의 리턴값으로 사용할 수 있다는 것을 의미한다.

def square(x):
    return x * x

print(square(5))
f = square

# 변수에 할당된 square 함수를 호출
print(f(4))

# 같은 메모리에 있는 함수 square을 출력
print(square)
print(f)


radius_list = [1, 2, 3, 4]


def circum(r):
    return round(2 * 3.14 * r, 2)


def area(r):
    return round(3.14 * r * r, 2)


def do_func(func, arg_list):
    result_list = []
    for arg in arg_list:
        result_list.append(func(arg))
    return result_list


result = do_func(circum, radius_list)
print(result)

result = do_func(area, radius_list)
print(result)


# 함수의 결과로 다른 함수를 리턴
def logger(msg):
    def log_message():
        print('log: {}'.format(msg))

    return log_message

log1 = logger('here')
print(log1)
log1()

del logger

try:
    print(logger)
except NameError:
    print('NameError: func not exists')

log1()


# 단순한 일반 함수
def simple_html_tag(tag, msg):
    print('<{0}>{1}<{0}>'.format(tag, msg))


simple_html_tag('h1', '심플 헤딩 타이틀')


# 함수를 리턴하는 함수
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))
    return wrap_text


print_h1 = html_tag('h1')
print_h1('첫 번째 헤딩 타이틀')
print_h1('두 번째 헤딩 타이틀')

print_p = html_tag('p')
print_p('이것은 패러그래프 입니다.')






