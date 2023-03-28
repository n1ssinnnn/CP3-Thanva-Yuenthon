menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("----My Food----")
    for food in range(len(menuList)):
        print(menuList[food],priceList[food])
        totalPrice += int(priceList[food])
    print("Total : ",totalPrice)

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()

