
# Подію додавання нового студента до групи необхідно фіксувати у лог-файлі.

# import logging
# logger=logging.getLogger("logging.py")
#
# logger.setLevel(logging.INFO)
#
#
# formatter=logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s')
#
# cons=logging.StreamHandler()
# cons.setLevel(logging.WARNING)
# cons.setFormatter(formatter)
#
#
#
# file=logging.FileHandler("logs/my_log.log")
# file.setLevel(logging.INFO)
# file.setFormatter(formatter)
#
# logger.addHandler(file)
# logger.addHandler(cons)
#
#
#
#
# if __name__ =='logging.py':
#     logger.info("Add student")
#     logger.warning("Something was wrong")



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
    potatoes=Goods("Potatoes",0,'vegetables')
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
