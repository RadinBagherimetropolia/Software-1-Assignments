class Food:
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories

    def print_info(self):
        print(f"{self.name}, has {self.calories} amount of calories")

#subclasses
class Fruit(Food):
    def __init__(self, name, calories, is_sweet):
        super().__init__(name, calories)
        self.is_sweet = is_sweet

    def print_info(self):
        super().print_info()
        print(f"sweet: {'Yes' if self.is_sweet else 'No'}")


class Vegetables(Food):
    def __init__(self, name, calories, is_leafy):
        super().__init__(name, calories)
        self.is_leafy = is_leafy

    def print_info(self):
        super().print_info()
        print(f"leafy: {'Yes' if self.is_leafy else 'No'}")

class Store:
    def __init__(self):
        self.inventory = {}

    def add_items(self,food_obj):
        self.inventory[food_obj.name.lower()] = food_obj

    def buy_items(self,name):
        name = name.lower()
        if name in self.inventory:
            return self.inventory[name]
        else:
            return None


    def print_info(self):
        print("Available items: ")
        for i in self.inventory.values():
            i.print_info()

class Smoothie:
    def __init__(self,name,ingredients):
        self.name = name
        self.ingredients = ingredients

        total = 0
        for i in ingredients:
            total += i.calories
        self.total_calories = total

    def smoothie_info(self):
        print(f"smoothie name: {self.name}")
        print("ingredients: ")
        for i in self.ingredients:
            print("-", i.name)
        print("total calories: ", self.total_calories)









#main program
b = Fruit("apple", 20, True)
c = Vegetables("carrot", 50, False)
smarket = Store()
smarket.add_items(b)
smarket.add_items(c)
smarket.add_items(Fruit("Banana", 70, True))
smarket.add_items(Fruit("Tomato", 50, False))
smarket.add_items(Vegetables("kale", 18, True))
smarket.add_items(Vegetables("cucumber", 10, False))

Ingredients = []
print("welcome to the s-market")
smarket.print_info()

while True:
    i = input("add an ingredient to your smoothie(empty to quit): ")
    if i == "":
        break

    product = smarket.buy_items(i)
    if product:
        Ingredients.append(product)
        print(f"added {product.name}")
    else:
        print("no such ingredient")
if len(Ingredients) == 0:
    print("no ingredients added")
smoothie = Smoothie("Best one", Ingredients)
smoothie.smoothie_info()


