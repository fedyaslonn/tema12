'''
Класс «Товар» содержит следующие закрытые поля:
● название товара
● название магазина, в котором подаётся товар
● стоимость товара в рублях
Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
● вывод информации о товаре со склада по индексу
● вывод информации о товаре со склада по имени товара
● сортировка товаров по названию, по магазину и по цене
● перегруженная операция сложения товаров по цене
'''
class Tovar:
    def __init__(self, name, shop_name, price):
        self.__name = name
        self.__shop_name = shop_name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_shop_name(self):
        return self.__shop_name

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Название товара: {self.__name}, Магазин: {self.__shop_name}, Цена: {self.__price}"


class Sklad:
    def __init__(self):
        self.__tovars = []

    def add_tovar(self, tovar):
        self.__tovars.append(tovar)

    def find_tovar(self, index):
        for indx, tovar in enumerate(self.__tovars):
            if indx == index:
                return str(tovar)
        return "Товар с таким индексом не найден"
    def find_tovar_by_name(self, name):
        for tovar in self.__tovars:
            if tovar.get_name() == name:
                return str(tovar)
        return "Товар с таким именем не найден"

    def sort_by_name(self):
        return sorted(self.__tovars, key=lambda tovar: tovar.get_name())

    def sort_by_shop(self):
        return sorted(self.__tovars, key=lambda shop: shop.get_shop_name())

    def sort_by_price(self):
        return sorted(self.__tovars, key=lambda price: price.get_price())

    def get_total_price(self):
        tot_sum = 0
        for tovar in self.__tovars:
            tot_sum += tovar.get_price()
        return tot_sum

    def __add__(self, other):
        if isinstance(other, Sklad):
            new_sklad = Sklad()
            new_sklad.__tovars = self.__tovars + other.__tovars
            return new_sklad
        return "Несовпадение типов"


sklad = Sklad()
sklad.add_tovar(Tovar("Товар7", "Магазин1", 135))
sklad.add_tovar(Tovar("Товар2", "Магазин5", 113))
sklad.add_tovar(Tovar("Товар3", "Магазин3", 300))
sklad.add_tovar(Tovar("Товар1", "Магазин2", 200))
print(sklad.find_tovar(4))
print(sklad.find_tovar(1))
print(sklad.find_tovar_by_name("Товар1"))  # Выведет информацию о товаре "Товар1"
print(sklad.find_tovar_by_name("Товар4"))
for tovar in sklad.sort_by_name():
    print(tovar)
for shop in sklad.sort_by_shop():
    print(shop)
for price in sklad.sort_by_price():
    print(price)
sklad1 = Sklad()
sklad2 = Sklad()
sklad3 = Sklad()
sklad1.add_tovar(Tovar("Товар1", "Магазин1", 100))
sklad2.add_tovar(Tovar("Товар1", "Магазин1", 100))
sklad3.add_tovar(Tovar("Товар1", "Магазин1", 100))
res = sklad1 + sklad2 + sklad3
print(res.get_total_price())