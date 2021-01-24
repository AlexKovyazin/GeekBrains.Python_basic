from itertools import cycle, count


def a_func(start_num, stop_num=20):
    for num in count(start_num):
        if num > stop_num:
            break
        yield num


def b_func(your_list, counter=10):
    cnt = 1
    for el in cycle(your_list):
        if cnt > counter:
            break
        yield el
        cnt += 1


test_list = [10, 20, 30, 40, 50]

for element in a_func(10):
    print(element)

print('*' * 50)

for element in b_func(test_list):
    print(element)
