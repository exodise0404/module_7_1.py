from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

class Shop():
    __file_name = 'products.txt'
    def get_products(self):
        self.__filename = 'products.txt'
        file = open(self.__filename, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for prod in products:
            if str(prod) not in Shop.get_products(self):
                file.write(str(prod) + '\n')
            else:
                print(f'Продукт {str(prod)} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
