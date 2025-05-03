from typing import List

class Pizza:
    # Атрибуты класса (общие для всех пицц)
    base = "тонкое тесто"
    cheese_type = "моцарелла"

    def __init__(self, name: str, toppings: List[str], size: str, price: float, is_spicy: bool):
        # Атрибуты объекта (у каждой пиццы свои)
        self.name = name
        self.toppings = toppings
        self.size = size
        self.price = price
        self.is_spicy = is_spicy
        self.is_baked = False

    def __str__(self):
        return f"Пицца '{self.name}' ({self.size}), {', '.join(self.toppings)}"

    def bake(self):
        if not self.is_baked:
            self.is_baked = True
            return f"Пицца '{self.name}' готова!"
        return "Эта пицца уже была приготовлена."

    def add_topping(self, topping: str):
        self.toppings.append(topping)
        return f"Добавлен топпинг: {topping}"

    def check_spicy(self):
        return "Острая!" if self.is_spicy else "Не острая."

    @classmethod
    def change_cheese(cls, new_cheese: str):
        cls.cheese_type = new_cheese


margherita = Pizza(
    name="Маргарита",
    toppings=["томаты", "базилик"],
    size="L",
    price=450,
    is_spicy=False
)

pepperoni = Pizza(
    name="Пепперони",
    toppings=["пепперони", "оливки"],
    size="XL",
    price=600,
    is_spicy=True
)


print(margherita)  
print(pepperoni.bake()) 
print(pepperoni.check_spicy())  

Pizza.change_cheese("чеддер")
print(f"Теперь во всех пиццах сыр: {Pizza.cheese_type}")  