# KOH WEI MING
# TP069308

groceries = []


# function for admin login access

def admin_login():
    while True:
        print("\n====================================================")
        print("-----------WELCOME TO ADMIN PAGE!------------")
        print("====================================================")
        print("Please Login to Access The System")

        print("\nUsername: ")
        admin_username = input()

        print("\nPassword: ")
        admin_password = input()

        if admin_username == "bryan" and admin_password == "Admin123":
            print("Login Attempt Successful")
            admin_menu()

        else:
            print("Login Attempt Failed")
            print("Incorrect Username or Password")

            c = input("Press 1 to Try Again, Press 2 to Exit. ")

            if c == "1":
                admin_login()

            else:
                print("Thank you Have A Great Day ")
                menu()


# function for admin menu

def admin_menu():
    while True:
        print("\n====================================================")
        print("-----------WELCOME ADMIN!------------")
        print("====================================================")

        print("Menu: ")
        print("1. Add Details of Groceries. ")
        print("\n2. Modify Groceries Information. ")
        print("\n3. View All Uploaded Groceries. ")
        print("\n4. Search Specific Groceries Detail. ")
        print("\n5. View All Orders of Customers. ")
        print("\n6. Search Order of Specific Customer. ")
        print("7. EXIT")

        choice = int(input("Please select from the choices given. "))

        if choice == 1:
            adddetailgroceries()

        elif choice == 2:
            modifygroceries()

        elif choice == 3:
            viewuploadedgroceries()

        elif choice == 4:
            searchspecificgroceries()

        elif choice == 5:
            viewordersofcustomer()

        elif choice == 6:
            searchspecificorderofcustomer()

        elif choice == 7:
            print("Thank You! See you again. ")
            menu()

        else:
            print("--Incorrect Input--")
            admin_menu()


# function of adding groceries details

def adddetailgroceries():
    while True:
        print("\n====================================================")
        print("-----------ADD GROCERY DETAILS------------")
        print("====================================================")

        print("Please fill in the grocery details in the form below. ")

        grocery = {}
        grocery['name'] = input("Grocery Name: ")
        while True:
            try:
                grocery['brand'] = input("Groccery Brand: ")
                break
            except:
                print('Enter numeric figure')
        while True:
            try:
                grocery['expdate'] = input("Grocery Expired Date: ")
                break
            except:
                print('Enter numeric figure')
        while True:
            try:
                grocery['price'] = int(input('Grocery Price: '))
                break
            except:
                print('Enter numeric figure')
        while True:
            try:
                grocery['specification'] = input("Grocery Specification: ")
                break
            except:
                print('Enter numeric figure')
        while True:
            try:
                grocery['quantity'] = int(input('Grocery Quantity: '))
                break
            except:
                print('Enter numeric figure')
        print(' Grocery has been successfully added.')
        groceries.append(grocery)
        admin_menu()


# function of modify groceries information

def modifygroceries():
    print("\n====================================================")
    print("-----------MODIFY GROCERY------------")
    print("====================================================")

    grocery_name = input('Enter the name of the grocery that you want to modify : ')
    for grocery in groceries:
        if grocery_name.lower() == grocery['name'].lower():
            print('current details of ' + grocery_name)
            print(grocery)
            grocery['name'] = input('Grocery name : ')
            while True:
                try:
                    grocery['brand'] = input("Groccery Brand: ")
                    break
                except:
                    print('Enter numeric figure')
            while True:
                try:
                    grocery['expdate'] = input("Grocery Expired Date: ")
                    break
                except:
                    print('Enter numeric figure')
            while True:
                try:
                    grocery['price'] = int(input('Grocery Price: '))
                    break
                except:
                    print('Enter numeric figure')
            while True:
                try:
                    grocery['specification'] = input("Grocery Specification: ")
                    break
                except:
                    print('Enter numeric figure')
            while True:
                try:
                    grocery['quantity'] = int(input('Grocery Quantity: '))
                    break
                except:
                    print('Enter numeric figure')
            print(' Grocery has been successfully added.')
            print(grocery)
        else:
            print('Grocery not found.')


# function for view groceries

def viewuploadedgroceries():
    print("\n====================================================")
    print("-----------VIEW UPLOADED GROCERIES------------")
    print("====================================================")
    print('Total inventory are: ', len(groceries))
    while len(groceries) != 0:
        print('Available groceries. ')
        for grocery in groceries:
            print(grocery['name'], ':', grocery['price'])
        break


# function for search specific groceries

def searchspecificgroceries():
    print("\n====================================================")
    print("-----------SEARCH SPECIFIC GROCERIES------------")
    print("====================================================")
    search_grocery = input('Enter the grocery\'s name to search in inventory : ')
    for grocery in groceries:
        if grocery['name'].lower() == search_grocery.lower():
            print(' The grocery named ' + search_grocery + ' is displayed below with its details. ')
            print(grocery)
        else:
            print('Incorrect Item. ')


# function for view all orders of customer

def viewordersofcustomer():
    print("\n====================================================")
    print("-----------VIEW ALL ORDERS OF CUSTOMER------------")
    print("====================================================")
    print("These are the details of customer order for specific time duration: ")

    orders_file = open("orders.txt")

    record = 0
    for orders_records in orders_file:
        orders_records = orders_records.strip('\n')
        print("[',(record + 1),']"), orders_records
        record += 1
    orders_file.close()

    back_exit = input("Do you want to go BACK or EXIT? (B,E): ")

    if back_exit == 'B':
        admin_menu()
    else:
        print("----Thank You!----")
        menu()


# function of search order of specific customer

def searchspecificorderofcustomer():
    print("\n====================================================")
    print("-----------SEARCH ORDER OF SPECIFIC CUSTOMER------------")
    print("====================================================")
    print("\nPlease use Customer Name to search specific customer payment: ")

    search_customer = input("Please enter Customer Name : ").upper()

    def searchorder():
        orders_file = open("orders.txt", "r")

        for customer in orders_file:
            if search_customer in customer:
                customer = customer.strip()
                value = customer.split(",")
                print(
                    "Records: \n\t1. Order type \n\t2. Bank Name \n\t3. Customer Name \n\t4. Account Number \n\t5. Total Order ")
                choice = input("Please key in the number of record you are looking for: ")

                if choice == '1':
                    print('\nOrder Type: ', value[0])
                elif choice == '2':
                    print('\nBank Name: ', value[1])
                elif choice == '3':
                    print('\nCustomer Name: ', value[2])
                elif choice == '4':
                    print('\nAccount Number: ', value[3])
                elif choice == '5':
                    print('\nTotal Payment: ', value[6])
                else:
                    print("\n--Incorrect Input--\n")
                    searchorder()
                orders_file.close()
                back_exit = input("Do you want to go BACK or EXIT? (B,E): ")

                if back_exit == 'B':
                    searchorder()
                else:
                    print("----Thank You!----")
                    admin_menu()
        else:
            print("!!! Incorrect Input !!!")
            orders_file.close()
            searchspecificorderofcustomer()

    searchorder()


# function for new customer

customer = []


def newcustomer_menu():
    print("\n====================================================")
    print("-----------WELCOME TO NEW CUSTOMER SIGN UP PAGE!------------")
    print("====================================================")
    print("1. View grocery\n2. Sign Up\n3. Exit")
    choice = input('Enter the number of your choice: ')

    if choice == '1':
        print("\n====================================================")
        print("-----------VIEW GROCERY PAGE!------------")
        print("====================================================")
        print('Total inventory are : ', len(groceries))
        while len(items) != 0:
            print('Available items. ')
            for grocery in groceries:
                for key, value in grocery.groceries():
                    print(key, ':', value)
            break
    elif choice == '2':
        newcustomer_signup()

    elif choice == '3':
        print("Thank you!")
        menu()


def newcustomer_signup():
    print("\n====================================================")
    print("-----------WELCOME TO NEW CUSTOMER SIGN UP PAGE!------------")
    print("====================================================")
    print("Please Fill The Form to Access The System")

    data = {}
    data['name'] = input("Customer Name: ")
    while True:
        try:
            data['username'] = input("Customer Username: ")
            break
        except:
            print('Incorrect Input')
    while True:
        try:
            data['password'] = input("Customer Password: ")
            break
        except:
            print('Incorrect Input')
    while True:
        try:
            data['rewritepassword'] = input("Customer Rewrite Password: ")
            break
        except:
            print('Incorrect Input')
    while True:
        try:
            data['address'] = input("Customer Address: ")
            break
        except:
            print('Incorrect Input')
    while True:
        try:
            data['bank detail'] = input("Customer Bank Detail: ")
            break
        except:
            print('Incorrect Input')
    while True:
        try:
            data['email'] = input("Customer Email ID: ")
            break
        except:
            print('Incorrect Input')
    while True:
        try:
            data['contact'] = input("Customer Contact Number: ")
            break
        except:
            print('Incorrect Input')
    while True:
        try:
            data['gender'] = input("Customer Gender: ")
            break
        except:
            print('Incorrect Input')
    while True:
        try:
            data['dateofbirth'] = input("Customer Date of Birth: ")
            break
        except:
            print('Incorrect Input')
    print('Customer has been successfully added.')
    customer.append(data)
    return data
    newcustomer_menu()


# function for registered customer

def customer_login():
    while True:
        print("\n====================================================")
        print("-----------WELCOME TO CUSTOMER LOGIN PAGE!------------")
        print("====================================================")
        print("Please Login to Access The System")

        print("\nUsername: ")
        customer_username = input()

        print("\nPassword: ")
        customer_password = input()

        for data in customer:
            if customer_username.lower() == data['username'].lower() and customer_password.lower() == data[
                'password'].lower():
                print('Welcome,', customer_username, '!')
                customer_menu()
            else:
                print('Login Attempt Failed')
                print('Incorrect Username or Password')

                p = input("Press 1 to Try Again, Press 2 to Exit. ")

                if p == '1':
                    customer_login()

                else:
                    print("Thank you Have A Great Day ")
                    menu()


# function for customer menu

def customer_menu():
    while True:
        print("\n====================================================")
        print("-----------WELCOME TO CUSTOMER MENU!------------")
        print("====================================================")
        print("Menu:")
        print(
            '1. View grocery\n2. Place order of groceries and do payment\n3. View order\n4.View personal information\n5. Exit')
        choice = input("Please select from the choices given. ")

        if choice == '1':
            print("\n====================================================")
            print("-----------VIEW GROCERY PAGE!------------")
            print("====================================================")
            print('Total inventory are : ', len(groceries))
            while len(items) != 0:
                print('Available items. ')
                for grocery in groceries:
                    for key, value in grocery.groceries():
                        print(key, ':', value)
                break

        elif choice == '2':
            print("\n====================================================")
            print("-----------PURCHASE GROCERIES PAGE!------------")
            print("====================================================")
            print(groceries)
            purchase_grocery = input('Which grocery do you want to buy? Enter name: ')
            for grocery in groceries:
                if purchase_grocery.lower() == grocery['name'].lower():
                    if grocery['quantity'] != 0:
                        print('Pay ', grocery['price'])
                        grocery['quantity'] -= 1
                    else:
                        print('grocery out of stock. ')

            choice = input(
                "\nPlease check the details shown above. \nPress 1 to Make Payment\nelse to go back to purchase page: ")
            if choice == '1':
                print("Please fill in the details required in the form below: ")
                payment_type = input("Payment Type: ")
                bankname = input("Bank Name: ")
                customer = input("Customer Name: ")
                accountnumber = input("Account Number: ").upper()
                expirydate = input("Card Exipiry Date (xx/xx): ")
                ccv = input("CCV : ")
                totalpayment = input("Total Payment Made: ")

                op = input(
                    "\nPlease check the detail shown above.\nPress 1 continue to make payment\n 2 To go back to make changes/cancelpayment: ")
                if choice == '1':
                    f = open('orders.txt', "r")
                    f.write(
                        '\n' + payment_type + ',' + bankname + ',' + customer + ',' + accountnumber + ',' + expirydate + ',' + ccv + ',' + totalpayment)
                    f.close()

                    print("PAYMENT PROCESSING...")
                    print("PAYMENT VERIFYING...")
                    print("!!! PAYMENT COMPLETED!!!")
                    print("You are now directed back to Registered Customer's Menu")
                    customer_menu()
                else:
                    print("!!! PAYMENT CANCELLED !!!")
                    print("You are now directed back to the top of page.")
                    customer_purchase()
            else:
                print("You are now directed back to the top of page.")
                customer_purchase()

        elif choice == '3':
            print("\n====================================================")
            print("-----------VIEW ORDER PAGE!------------")
            print("====================================================")

            try:
                filehandler = open('orders.txt')
                for word in filehandler:
                    print(word)
            except:
                print('File cannot be opened: ')
                customer_menu()
            filehandler.close()

        elif choice == '4':
            print("\n====================================================")
            print("-----------VIEW PERSONAL INFORMATION PAGE!------------")
            print("====================================================")

            for data in customer:
                print('name: ', data['name'])


        elif choice == '5':
            print('Thank You, See You Again. ')
            customer_menu()

        else:
            print('Error')
            menu()


# function for customer purchase grocery
def customer_purchase():
    print("\n====================================================")
    print("-----------PURCHASE GROCERIES PAGE!------------")
    print("====================================================")
    print(groceries)
    purchase_grocery = input('Which grocery do you want to buy? Enter name: ')
    for grocery in groceries:
        if purchase_grocery.lower() == grocery['name'].lower():
            if grocery['quantity'] != 0:
                print('Pay ', grocery['price'])
                grocery['quantity'] -= 1
            else:
                print('grocery out of stock. ')

    choice = input(
        "\n Please check the details shown above. \nPress 1 to Make Payment\n else to go back to purchase page: ")
    if choice == '1':
        print("Please fill in the details required in the form below: ")
        payment_type = input("Payment Type: ")
        bankname = input("Bank Name: ")
        customer = input(" Customer Name: ")
        accountnumber = input("Account Number: ").upper()
        expirydate = input("Card Exipiry Date (xx/xx): ")
        ccv = input("CCV : ")
        totalpayment = input("Total Payment Made: ")

        op = input(
            "\nPlease check the detail hown above.\nPress 1 to make payment\n 2 To go back to make changes/cancelpayment: ")
        if choice == '1':
            f = open('orders.txt', "r")
            f.write(
                '\n' + payment_type + ',' + bankname + ',' + customer + ',' + accountnumber + ',' + expirydate + ',' + ccv + ',' + totalpayment)
            f.close()

            print("PAYMENT PROCESSING...")
            print("PAYMENT VERIFYING...")
            print("!!! PAYMENT COMPLETED!!!")
            print("You are now directed back to Registered Customer's Menu")
            customer_menu()
        else:
            print("!!! PAYMENT CANCELLED !!!")
            print("You are now directed back to the top of page.")
            customer_purchase()
    else:
        print("You are now directed back to the top of page.")
        customer_purchase()

    # Main Menu function


def menu():
    while True:
        print("\n====================================================")
        print("-----------WELCOME TO FRESHCO SDN BHD!------------")
        print("====================================================")
        print("Select the operation that you want to perform:")
        print("\t1. Admin \n\t2. New Customer \n\t3. Registered Customer")
        choice = (input(" Enter selection:"))

        if choice == '1':
            admin_login()

        elif choice == '2':
            newcustomer_menu()

        elif choice == '3':
            customer_login()

        else:
            print("\n-- Incorrect Choice --\n")


menu()
