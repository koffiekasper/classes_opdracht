import opdracht

algernon = opdracht.Book('Flowers for Algernon', '10', 'Daniel Keyes')
cryptonomicon = opdracht.Book('Cryptonomicon', '15', 'Neal Stephenson')
jeansMale = opdracht.Clothes('Jeans', 40, 34, 'M')
jeansFemale = opdracht.Clothes('Jeans', 40, 34, 'F')
beer = opdracht.Product('Beer', 1)

initItems = [algernon, cryptonomicon, jeansMale, jeansFemale, beer]
for item in initItems:
    opdracht.products.append(item)

owner = opdracht.Owner()
customer = opdracht.Customer()

def uiQuestion(questionList):
    print('\t- - -')    
    for i in range(len(questionList)):
        print(f'\t[{i+1}] - {questionList[i]}')
    return int(input(('Pick a number:')))-1

def enterFive():
    for i in range(5):
        print()

def invalidInput():
    input("Invalid input! [ENTER to continue]")
    enterFive()
    return

def addProduct():
    type = uiQuestion(["Normal product", "Book", "Clothes"])
    name = input("Product name:")
    price = int(input("Price in euros:"))
    if type == 0:
        prod = opdracht.Product(name, price)
    if type == 1:
        author = input("Author name:")
        prod = opdracht.Book(name, price, author)
    if type == 2:
        size = input("Enter clothes size (S/M/L/XL)")
        gender = uiQuestion(["Male", "Female"])
        if gender == 0:
            gender = "M"
        elif gender == 1:
            gender == "F"
        prod = opdracht.Clothes(name, price, size, gender)
    opdracht.products.append(prod) 
    enterFive()
    input("Product added!")

def ownerUI():
    enterFive()
    ans = uiQuestion(['Add product', 'Remove product', 'Back'])
    if ans == 0:
        addProduct()
    if ans == 1:
        ans2 = uiQuestion([prod.name for prod in opdracht.products])
        opdracht.products.pop(ans2)
        input("Removed! ENTER to continue")
    if ans == 2:
        return

def renderCustomerInfo(customer):
    print(f'Balance: {str(customer.balance.getAmount())}')
    if len(customer.cart.getItems()) > 0:
        print("\tCart:")
        for item in customer.cart.getItems():
            print("\t" + item.name)

def addToCart(customer):
    ans = uiQuestion([prod.name for prod in opdracht.products])
    customer.cart.addItem(opdracht.products[ans])
    input("Item added to cart! [ENTER to continue]")
    enterFive()


def customerUI(customer):
    while True:
        renderCustomerInfo(customer)
        input("ENTER to continue")
        ans = uiQuestion(["Add item to cart", "Add money balance", "Check-out", "Back"])
        if ans == 0:
            addToCart(customer)
        elif ans == 1:
            ans = uiQuestion(["10", "20", "30"])
            customer.addMoney((ans+1)*10)
            input("Money added! [ENTER to continue]")
            enterFive()
        elif ans == 2:
            if customer.checkout() == True:
                input("Items purchased!")
                enterFive()
            else:
                input("You don't have enough money!")
                enterFive()
        elif ans == 3:
            return

while True:
    input("Welcome! [ENTER to continue]")
    while True:
        enterFive()

        ans = uiQuestion(['Log-in as owner', 'Log-in as customer'])
        if ans == 0:
            enterFive()
            ownerUI()
        elif ans == 1:
            enterFive()
            customerUI(customer)
        else:
            invalidInput()