
# 1) Створіть декоратор, який підраховуватиме, скільки разів була
# викликана функція, що декорується.

def quantity_function(func):
    count = False
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        res = count
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
# 3) Припустимо, у класі визначено метод __str__, який повертає  рядок виходячи з класу. Створіть такий декоратор для цього методу,
# щоб отриманий рядок зберігався у текстовий файл, ім'я якого збігається з ім'ям класу, метод якого ви прикрашали.

def save_to_file(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        line = open("MyClass.txt", "w")
        line.write(res)
        line.close()
        return res
    return inner


class MyClass:
    def __init__(self, a, b):
        self.a,self.b = a,b

    @save_to_file
    def __str__(self):
        return f"MyClass (a = {self.a}, b = {self.b})"

x = MyClass(10, 100)
y=MyClass(1, 10)

print(x,y)


#
# 4) Створіть декоратор із параметрами для проведення хронометражу роботи
# тієї чи іншої функції. Параметрами повинні виступати те, скільки разів потрібно
# запустити функцію, що декорується, і в який файл зберегти результати
# хронометражу. Мета - провести хронометраж функції, що декорується.

def timekeeping(num=1, fname="myfile.txt"):
    def dec(func):
        def inner(*args):
            i = 0
            start = time.time()
            while i < num:
                res = func(*args)
                i += 1
            stop = time.time()
            file = open(fname, "w")
            file.write(f" Lead time = {stop - start} sec")
            file.close()
            return res
        return inner
    return dec

import time
@timekeeping(2)
def palindrome():
    list,list_2 = [],[]
    for i in range(100, 1000):
        for j in range(100, 1000):
            product=i*j
            if str(product)[:]==str(product)[::-1] and len(str(product))==6:
                list.append(int(product))
                if i * j == max(list):
                    multiplier_1,multiplier_2=i,j
                    list_2.append(max(list))
    return  max(list_2)

print(palindrome())