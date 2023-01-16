# Напишіть_функцію-генератор, яка повертатиме прості числа.
#  Верхня межа діапазону повинна бути задана параметром цієї функції.
def prime_numbers(stop):
    for item in range(2, stop + 1):
        for num in range (2,item):
            if not item % num:
                break
        else:
            yield item


seq = prime_numbers(50)
for i in seq:
    print(i)
print('_'*56)

 # Реалізуйте_генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
 # Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при передачі команди на завершення.
def geom_progression(number,denominator):
    print(number)
    res=denominator*number
    while True:
        yield res
        number=res
        res=denominator*number

seq = geom_progression(5, 10)

for item in seq:
    if item > 50_000_000:
        seq.close()
    print(item)
print('_'*56)

# Реалізуйте_свій аналог генераторної функції range().
def unique_range(first_num, last_num = (), step = ()):
    if not last_num:
        last_num,first_num = first_num,0
    if not step:
        step = 1
    follow_ = first_num
    while follow_ < last_num:
        yield follow_
        first_num = follow_
        follow_ = first_num + step
seq = unique_range(1,5)

#
#
# print (next(seq))
# print (next(seq))
# print (next(seq))
# print (next(seq))
# print (next(seq))
# print (next(seq))
# print (next(seq))
# print (next(seq))
for item in seq:
    print(list(seq))
print('_'*56)


# Напишіть_генераторний вираз для заповнення списку.
#  Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.
import random
gen = (item**3 for item in range(random.randint(2,20)))
print(list(gen))