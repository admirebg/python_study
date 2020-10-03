# -*- coding: utf-8 -*-

# 제너레이터란
# iterator를 수동으로 작성하기 위해 yield를 사용하는 함수

num_list = [1, 2, 3, 4, 5]

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers(num_list)
print(my_nums)


def square_numbers_gen(nums):
    for i in nums:
        yield i*i   # 멈추고 돌아간 후 다음 next 시에 다시 와서 실행함

my_nums_gen = square_numbers_gen(num_list)
print(my_nums_gen)
print(dir(my_nums_gen))

print(next(my_nums_gen))
print(next(my_nums_gen))
print(next(my_nums_gen))
print(next(my_nums_gen))
print(next(my_nums_gen))

print(next(my_nums_gen))