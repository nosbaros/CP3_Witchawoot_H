usernameInput = input("Username :")
passwordInput = input("Password :")

if usernameInput == "admin" and passwordInput == "password":
    ricePrice = 30
    firshWaterPrice = 10
    sugarPrice = 15
    print("Welcome my NosShop")
    print("----- NosShop -----")
    print("1. ข้าวสาร ราคา", ricePrice, "บาท")
    print("2. น้ำปลา ราคา", firshWaterPrice, "บาท")
    print("3. น้ำตาล ราคา", sugarPrice, "บาท")
    selectX = int(input("เลือกสินค้า : "))
    if selectX == 1:
        countX = int(input("ใส่จำนวนสินค้า : "))
        print("คุณซื้อ ข้าวสาร ราคา : ", ricePrice, "บาท จำนวน : ", countX, "รวมเป็นเงิน : ",
              int(ricePrice * countX))
    elif selectX == 2:
        countX = int(input("ใส่จำนวนสินค้า : "))
        print("คุณซื้อ น้ำปลา ราคา : ", firshWaterPrice, "บาท จำนวน : ", countX, "รวมเป็นเงิน : ",
              int(firshWaterPrice * countX))
    elif selectX == 3:
        countX = int(input("ใส่จำนวนสินค้า : "))
        print("คุณซื้อ น้ำตาล ราคา : ", sugarPrice, "บาท จำนวน : ", countX, "รวมเป็นเงิน : ",
              int(sugarPrice * countX))
    else:
        print("คุณเลือกสินค้าไม่ถูกต้อง")
else:
    print("User Or Password wrong !")