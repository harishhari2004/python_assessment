class Product:
    def _init_(self, pid, name, price, stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock


class ShoppingCart:
    def _init_(self):
        self.cart = {}

    def add_product(self, products, pid, qty):

        if pid not in products:
            print("Product does not exist")
        elif qty <= 0:
            print("Invalid quantity")
        elif products[pid].stock < qty:
            print("Insufficient stock")
        else:
            if pid in self.cart:
                self.cart[pid][1] += qty
            else:
                self.cart[pid] = [products[pid], qty]

            products[pid].stock -= qty

    def remove_product(self, pid, qty):

        if pid not in self.cart:
            print("Product not in cart")
        elif qty <= 0:
            print("Invalid quantity")
        elif self.cart[pid][1] < qty:
            print("Insufficient quantity in cart")
        else:
            self.cart[pid][1] -= qty
            self.cart[pid][0].stock += qty

            if self.cart[pid][1] == 0:
                del self.cart[pid]

    def calculate_total(self):

        total = 0

        for product, qty in self.cart.values():
            total += product.price * qty

        return total

    def display_cart(self):

        if not self.cart:
            print("Cart is empty")
            return

        for product, qty in self.cart.values():
            subtotal = product.price * qty

            print(f"{product.name} - Quantity: {qty} - Subtotal: {subtotal}")

        total = self.calculate_total()

        if total >= 20000:
            discount = 15
        elif total >= 10000:
            discount = 10
        elif total >= 5000:
            discount = 5
        else:
            discount = 0

        discount_amount = total * discount / 100
        final_amount = total - discount_amount

        print("\nTotal Amount:", total)
        print("Discount:", str(discount) + "%")
        print("Discount Amount:", f"{discount_amount:.0f}")
        print("Final Amount:", f"{final_amount:.0f}")


# Main program

n = int(input())

products = {}

for i in range(n):

    pid, name, price, stock = input().split()

    products[pid] = Product(pid, name, float(price), int(stock))


cart = ShoppingCart()

operations = int(input())

for i in range(operations):

    operation = input().split()

    if operation[0] == "ADD":
        cart.add_product(products, operation[1], int(operation[2]))

    elif operation[0] == "REMOVE":
        cart.remove_product(operation[1], int(operation[2]))

    elif operation[0] == "TOTAL":
        print("Total:", f"{cart.calculate_total():.0f}")

    elif operation[0] == "DISPLAY":
        cart.display_cart()