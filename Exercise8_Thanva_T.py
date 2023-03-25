n1input = input("Username : ")
pasinput = input("Password : ")

if n1input == "N1ssin" and pasinput == "UWU":
    print("Login success !")
    print("----------MainMenu----------")
    print("1.Cola 15 THB")
    print("2.Orange juice 10 THB")
    userSelected = int(input(">>"))
    if userSelected == 1:
        print("How many do you want ?")
        Cola = 15
        price = int(input())
        result1 = Cola * price
        print(str(result1)+"THB")
        print("Thank you for shopping with us UWU")
    elif userSelected == 2:
        print("How many do you want ?")
        Orangejuice = 10
        price = int(input())
        result2 = Orangejuice * price
        print(str(result2) + "THB")
        print("Thank you for shopping with us UWU")
