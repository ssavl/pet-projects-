class Goods:

    def __init__(self, name, price, stock=0, discount=0, max_discount=0):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название слишком короткое')
        self.price = abs(float(price))
        self.stock = abs(float(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая скидка')
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def discounted(self):
        return self.price - self.price * self.discount / 100

    def sell(self, item_count=1):
        if item_count > self.stock:
            raise ValueError('Недостаточно товаров на складе')
        # ТУТ МОЖНО СДЕЛАТЬ КАКОЙ-ТО ЗАПРОС В СИСТЕМУ УЧЕТА ТОВАРОВ
        self.stock -= item_count

    def __repr__(self):
        return f'Product name: {self.name}, price: {self.price}, stock: {self.stock}'


product1 = Goods('iphone', 100, stock=5)
product1.sell(2)
print(product1)