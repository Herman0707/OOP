
# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності,
# закон якої задається за допомогою функції користувача. Крім цього параметром генераторної функції повинні
# бути значення першого члена прогресії та кількість членів, що видаються послідовностю.
# Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.
#

def unique_func(num):
    return num**2

def generator (start, stop, unique_func):
    for i in range(stop):
        yield start
        start = unique_func(start)

print(*list(generator(2, 5, unique_func)))

print(16*"_")


# 2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація.
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі.
# Порівняйте швидкість виконання із просто рекурсивним підходом.
#

def mem (func):
    a = dict()
    def inside (*args):
        if args in a:
            return a[args]
        a[args]=func(*args)
        return a[args]
    return inside

# @mem
def fib(n):
    if n in (1,2):
        return 1
    return  fib(n-1)+fib(n-2)


fib=mem(fib)

import time

mem_time = time.process_time()
print(fib(40))
print(f"{time.process_time()-mem_time} sec")    # 102334155   using memoization
                                                # 0.0  sec

                                                # 102334155    without using Memoization
                                                # 18.078125 sec


# 3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого
# списку.

def sum_numbers():
    numbers=[]
    def inner (number):
        numbers.append(number)
        print(numbers)
        return sum(numbers)
    return inner

rez=sum_numbers()
print(rez(100))
print(rez(200))
print(rez(300))
print(rez(400))
print(rez(500))
