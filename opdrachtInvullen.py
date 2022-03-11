products = []

class Cart:
    def __init__(self):
        self.storage = []
    
    #Todo 4: Create an addItem function. This function takes an item (Product) and inserts it into the storage.

    #Todo 5: Create the other functions that appear in the class diagram.


#ToDo 1: Complete the product class. Use the class diagram and add the attributes and methods
class Product:




#ToDo 2: Make a Book class

#ToDo 3: Make a Clothes class

class Customer:
    def __init__(self):
        self.balance = Money()
        self.cart = Cart()
    
    #ToDo 7: add checkout method here. This function checks if the customer has enough money in his account. If so, the total price will be paid.
    

    def addMoney(self, val):
        return self.balance.addMoney(val)
    
class Owner:
    def addProduct(self, product):
        global products
        products.append(product)
        return True
    
    def removeProduct(self, product):
        global products
        for existingProduct in products:
            if existingProduct.name == product.name:
                products.remove(product)
                return True
        return False

#ToDo 6: Make a Money class. This class can check how much money a customer has in his virtual wallet.
#It can also add/remove money from the customer's wallet