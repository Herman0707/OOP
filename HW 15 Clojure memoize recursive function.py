
# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності,
# закон якої задається за допомогою функції користувача. Крім цього параметром генераторної функції повинні
# бути значення першого члена прогресії та кількість членів, що видаються послідовностю.
# Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.
#
#
#
# 2. Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація.
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі.
# Порівняйте швидкість виконання із просто рекурсивним підходом.
#
#
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
