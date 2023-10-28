class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self):
        return self.price

class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def calculate_price(self):
        
        shipping_cost = self.weight * 2
        return self.price + shipping_cost

class DigitalProduct(Product):
    def calculate_price(self):
        return self.price

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product):
        self.cart.remove(product)

    def calculate_total_price(self):
        total_price = sum(product.calculate_price() for product in self.cart)
        return total_price

    def checkout(self):
        total_price = self.calculate_total_price()
        print("Checkout successful.")
        print(f"Total Price: ${total_price:.2f}")
        print("Thank you for your purchase!")


physical_product = PhysicalProduct("Book", 15.99, 2.0)
digital_product = DigitalProduct("Ebook", 9.99)

cart = ShoppingCart()


cart.add_product(physical_product)
cart.add_product(digital_product)


total_price = cart.calculate_total_price()
print(f"Total Price in the cart: ${total_price:.2f}")


cart.checkout()
