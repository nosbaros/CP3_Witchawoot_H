usernameInput = input("Username :")
passwordInput = input("Password :")

if usernameInput == "admin" and passwordInput == "password":
    print("Done")
    print("---- iShot -----")
    print("1.Vat Caluator")
    print("2. Price Calulator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1+price2)
