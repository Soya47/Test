# Tay Hong Yi
# TP068258



def upload():
    print("Please enter the groceries that you wish to update")
    print("\nPlease upload it by this format: Grocery_Name(space) (Price(Enter only number)) (space) (Exp_Date:(DD/MM/YYYY)) (space) Brand:xxxxxx ")
    print("\n Please type None if there is no expired date or brand")

    uploadgrocery = input("\nPlease write the grocery over here")

    uploadgroceryfile = open("GroceryItems.txt", "a")
    uploadgroceryfile.write("\n")
    uploadgroceryfile.write(uploadgrocery)
    uploadgroceryfile.close()
    print("You have uploaded successfully!")




def modify():
    file = open("GroceryItems.txt", mode="r")
    groceryitem = file.read()
    print(groceryitem)
    file.close()
    oldupdatemodify = input("Please enter the full name of the grocery item or the grocery information that you wish to update or modify:")
    newupdatemodify = input("Please enter the following details that you wish to update:")
    groceryitem = groceryitem.replace(oldupdatemodify, newupdatemodify)
    with open("GroceryItems.txt", "w") as file:
        file.write(groceryitem)






def deletegroceryline(filename, line_num):
    with open(filename) as file:
        lines = file.readlines()

    if (line_num <= len(lines)):
        del lines[line_num - 1]
        print(lines)

        with open(filename, "w") as file:
            for line in lines:
                file.write(line)

    else:
        print("Line", line_num, "not in the file.")



def search():
    searchdetail = input(
        "Enter the full grocery name (with its capitalized alphabet) include '_' to search its deatail (Enter exit to exit this section):")

    file = open("GroceryItems.txt", "r")
    for line in file:
        if searchdetail in line:
            print(line)

    file.close()



def newregister():
    name = input("Please enter your name:")
    email = input("Please enter your email:")
    address = input("Please enter your address:")
    contact_num = input("Please enter your contact number:")
    gender = input("Please enter your gender: (M or F only)")
    date_of_birth = input("Please enter your date of birth:(YYYY/MM/DD)")
    userid = input("Please enter your user ID:")
    password = input("Please set your password:")
    rewrite_password = input("Please rewrite your password:")
    check = input("If the information you write is all correct, type c otherwise type re")
    while check != "c" and check != "re":
        check = input("Perhaps you have a typing error, please retype again:")
    if check == "c":
        # w mode will create a file for user and put their personal information inside the text file
        outfile = open(name, mode="w")
        outfile.write("Email:" + email)
        outfile.write("\nName:" + name)
        outfile.write("\nAddress:" + address)
        outfile.write("\nContact number:" + contact_num)
        outfile.write("\nGender:" + gender)
        outfile.write("\nDate of birth:" + date_of_birth)
        outfile.write("\nUser ID:" + userid)

        outfile.close()
    else:
        newregister()





itemAvailableDict={}
shoppingDict={}


print("*"*25)
print("Welcome to FRESHCO Grocery!")
type_of_user = input("For admin type 1, registered user type 2, new user type 3)")

while type_of_user != '1' and type_of_user != '2' and type_of_user != '3':
    type_of_user = input("Input 1 or 2 or 3")


if type_of_user == "1":
    # admin

    b = 1
    while b == 1:

        code = "adminaccess"
        type = input("Please enter the password to access the access system or type 'ex' to exit if u have misentered:")

        if type == "ex":
            print("Please restart our system to shop again!")
            break

        elif type == code:
            print("You have successfully login!\nHere are the following option to choose:")


            while b == 1  :

                print("\nIf you wish to upload grocerices detail, type 1")

                print("\nIf you wish to update/modify Groceries information, type 2")

                print("\nIf you wish to delete Groceries item and its information, type 3")

                print("\nIf you wish to search specific Groceries detail, type 4")

                print("\nIf you wish to view all orders of a specific customers, type 5")

                print("\nIf you wish to leave, type 6")

                choice = input("Please select a number")

                while choice != "1" and choice != "2" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
                    choice = input("Please select a number from 1 - 6 ONLY!")

                if choice == "1":
                    #upload grocerices detail

                    upload()

                elif choice == "2":
                    #update/modify Groceries information

                    modify()

                elif choice == "3":
                    # delete Groceries information

                    deletefilename = input("Please write the word 'GroceryItems.txt':")
                    deleteline_num = int(input("Please enter the line number:"))

                    deletegroceryline(deletefilename, deleteline_num)



                elif choice == "4":
                    #search specific Groceries detail

                    search()

                elif choice == "5":
                    #view all orders of a specific customers
                    searchorder = input("Please enter the customer name to search for its order:")
                    customerfile = open(searchorder,"r")
                    print(customerfile.read())
                    customerfile.close()


                else :
                    print("You have exit the sysytem!")
                    b = 0

                    # exit

        else:
            print("Please enter again as you have a typo")


elif type_of_user == "2":
    # registered user

    print("These are the following groceries and its detaiils in our shop!")
    file = open("GroceryItems.txt","r")
    itemsAvailable = file.read()
    print(itemsAvailable)
    file.close()


    a = 1
    while a == 1:

        try:
            registered_user = input(
                "Please enter your name to view your personal information and bill(if previously bought in our shop) and to place order of groceries (Please be aware of the capital letter of the username that you previously registered):")
            registered_file = open(registered_user, "r")
            registered_name = registered_file.read()
            print(registered_name)
            registered_file.close()
        except:

            print("You are not aregistered user!")
            break

        else:
            print("You have successfully login!\nHere are the following Grocery's Item and its corresponding price")

            file = open("GroceryItems.txt", mode="r")
            itemsAvailablelist = file.readlines()

            file.close()

            # to fetch an item from a list into a dict we can use for loop
            for item in itemsAvailablelist:

                # split turns string into list
                item_name = item.split()[0]
                item_price = item.split()[1]
                print(f"{item_name}:{item_price}")
                # print the item name and its corresponding price seperated by the colon (:)


                # .update added the items in the list to a dict
                itemAvailableDict.update({item_name:float(item_price)})

                # float to turn the string number into number that can be multiply

            buythings = input("Would you like to proceed or leave?(yes/no only)")


            while buythings.lower() == "yes":
                item_added = input("Please write the full name of the grocery to add in your cart:")
                #.title returns a string where the first character in every word is upper case
                if item_added.title() in itemAvailableDict:
                    qtyofitem = int(input("Please enter quantity:"))
                    shoppingDict.update({item_added:{"quantity":qtyofitem,'subtotal':itemAvailableDict[item_added.title()]*qtyofitem}})
                    print(shoppingDict)

                else:
                    print("Unable to add unavailable item")
                buythings = input("Do you wish to add more items?(yes/no)")
            orderfile = open(registered_user, mode="a")
            orderfile.write("\n\n")
            orderfile.write("Customer's Bill:")
            orderfile.write("\n")
            orderfile.write("*" * 20)
            orderfile.write("\n")
            orderfile.write("Item       Quantity      Subtotal")
            orderfile.write("\n")


            print("Item       Quantity      Subtotal")
            total=0

            for key in shoppingDict:

                totalitemqtysubtotal = (f"{key}         {shoppingDict[key]['quantity']}       {shoppingDict[key]['subtotal']}")
                print(totalitemqtysubtotal)

                total=shoppingDict[key]['subtotal']+total
                totalprice = str(total)
                print("Total:", totalprice)

                orderfile.write(totalitemqtysubtotal)
                orderfile.write("\n")
            orderfile.write("Total:")
            orderfile.write(str(total))
            orderfile.write("\n")

            orderfile.close()


        print("*********************")
        print("Thank you for visiting our grocery shop, hope to see you soon!")

        a = 0

else:
# new user

    print("Welcome to FRESHCO Grocery, new user!\nHere are the following Grocery's Item")
    file = open("GroceryItems.txt", mode="r")
    print(file.read())
    file.close()
    register_or_exit = input("If you wish to register,type r; if you wish to leave, type exit ")

    while register_or_exit != "r" and register_or_exit != "exit":
        register_or_exit = input("Perhaps you have a typing error, please retype again:")

    if register_or_exit == "r":

        newregister()

    else:
        print("Thanks for visiting our grocery shop! Have a nice day and bye!")


