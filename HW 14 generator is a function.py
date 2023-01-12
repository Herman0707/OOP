
 # 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
 # Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при передачі команди на завершення.

def geom_progression(number,denominator):
    print(number)
    res=denominator*number
    while True:
        yield res
        number=res
        res=denominator*number
    return res
seq = geom_progression(5, 10)

for item in seq:
    if item > 50_000_000:
        seq.close()
    print(item)


# 2. Реалізуйте свій аналог генераторної функції range().
# 3. Напишіть функцію-генератор, яка повертатиме прості числа.
#  Верхня межа діапазону повинна бути задана параметром цієї функції.
# 4. Напишіть генераторний вираз для заповнення списку.
#  Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.
import random
gen = (item**3 for item in range(random.randint(2,50)))
print(list(gen))