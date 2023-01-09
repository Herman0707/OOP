#
# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару, опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# 2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон тощо.
# 3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості. Замовлення має містити дані про користувача,
# який його здійснив. Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного виведення інформації про це замовлення.


# 4. Модифікуйте Перше домашнє завдання так, щоб при спробі встановити
# від'ємну або нульову вартість товару викликалася виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).

# 5.Модифікуєте клас Замовлення (завдання Лекції 1), додавши реалізацію протоколу послідовностей та ітераційного протоколу.



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

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.price_of_goods):
            self.index += 1
            return self.price_of_goods[self.index - 1]
        raise StopIteration

    def __str__(self):
        return f'{self.name} ({customerB})' +'\n' +'\n' +'\n'.join(map(str, self.list_of_goods)) + '\n' + f"{'_' * 44}" '\n'+ 'Total cost:  ' + f'{sum(map(int, self.price_of_goods))} UAH'

class Sequence_protocol:
    def __init__(self, number):
            self.number = number
    def __len__(self):
        return self.number
    def __getitem__(self, index):
        if isinstance(index, slice):
            if index.start < 0 or index.stop > self.number:
                raise IndexError
            else:
                result = []
                start = 0 if index.start == None else index.start
                stop = self.number - 1 if index.stop == None else index.stop
                step = 1 if index.step == None else index.step
                for i in range(start, stop, step):
                    result.append(i)
                return result
        if isinstance(index, int):
            if index < self.number:
                return index
            else:
                raise IndexError
        raise TypeError()



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

x=Sequence_protocol(6)
for i in x:
    print(i,end=" ")

print()

Total_cost=0
for price_of_goods in order_1:
    Total_cost+=price_of_goods
print(f"Total_cost: {Total_cost} UAH")

#