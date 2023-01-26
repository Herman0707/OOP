
# 1) Створіть декоратор, який підраховуватиме, скільки разів була
# викликана функція, що декорується.

def quantity_function(func):
    count = False
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        res = f'{func(*args, **kwargs)}, count: {count}'
        return res
    return inner

@quantity_function
def my_funcion(arg):
    return arg
print(my_funcion("hello"))
print(my_funcion("hello"))
print(my_funcion("hello"))

# 2) Створіть декоратор, який зареєструє декоровану функцію в
# списку функцій для обробки послідовності.

my_list = []

def add(func):
    my_list.append(func)
    return func

@add
def pow(item):
    return item**2
@add
def floor_div(item):
    return  item // 2
@add
def modul(item):
    return item % 2

print(*[func(100) for func in my_list])


#
# 3) Припустимо, у класі визначено метод __str__, який повертає
# рядок виходячи з класу. Створіть такий декоратор для цього методу,
# щоб отриманий рядок зберігався у текстовий файл, ім'я якого
# збігається з ім'ям класу, метод якого ви прикрашали.
#
# 4) Створіть декоратор із параметрами для проведення хронометражу роботи
# тієї чи іншої функції. Параметрами повинні виступати те, скільки разів потрібно
# запустити функцію, що декорується, і в який файл зберегти результати
# хронометражу. Мета - провести хронометраж функції, що декорується.
