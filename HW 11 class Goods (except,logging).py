#
# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару, опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон тощо.
# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості. Замовлення має містити дані про користувача,
# який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного виведення інформації про це замовлення.



# 1. Модифікуйте Перше домашнє завдання так, щоб при спробі встановити
# від'ємну або нульову вартість товару викликалася виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).




class Incorrect_price (Exception):
    def __init__(self, message):
        self.message=message
    def __str__(self):
        return f"{self.message}"


class Goods:
    def __init__(self, title, price, group_of_goods):
        if price <= 0:
            raise Incorrect_price("Sometimes was wrong")


        self.title = title
        self.price = price
        self.group_of_goods=group_of_goods


    def __str__(self):
        return f'{self.title}: {self.price} UAH, Group of goods: {self.group_of_goods}'



class Сustomer:
    def __init__(self, name,  surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number=phone_number

    def __str__(self):
        return f'{self.name} {self.surname}, phone_number: {self.phone_number}'



class Order:
    def __init__(self, name):
        self.name=name
        self.price_of_goods=[]
        self.list_of_goods = []

    def add (self, good:Goods):
        if good not in self.list_of_goods:
            self.list_of_goods.append(good)
            self.price_of_goods.append(good.price)

    def __str__(self):
        return f'{self.name} ({customerB})' +'\n' +'\n' +'\n'.join(map(str, self.list_of_goods)) + '\n' + f"{'_' * 44}" '\n'+ 'Total cost:  ' + f'{sum(map(int, self.price_of_goods))} UAH'

try:
    cherry=Goods("Cherry",100, "fruit")
    potatoes=Goods("Potatoes",2,'vegetables')
    limon=Goods("Limon",80,"fruit")


    customerA=Сustomer("Alexander","Panchuk", "+380930252500")
    customerB=Сustomer("Maksym","Evych","+380675544333")

    order_1 =Order("Consumer Order 09_12_2022")
    order_1.add(cherry)
    order_1.add(limon)
    order_1.add(potatoes)
    print(order_1)



except Incorrect_price:
    print("The price of the product is incorrect")


#