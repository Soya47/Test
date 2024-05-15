#LIM JIA YI
#TP068862

def user_admin_check(userid, username):
    if userid == "1":
        admin_menu()
    else:
        user_menu(username, userid)


def cs_info(username, final_username, userid):
    usernamedb = open("username.txt", "r")
    for line in usernamedb:
        if (not (line.find(username) == -1)):
            line = line.strip("\n")
            usernamelist = line.split(", ")
            usernamelist = list(usernamelist)
            userid = usernamelist[0]
    usernamedb.close()
    emaildb = open("email.txt", "r")
    for line in emaildb:
        if (not (line.find(userid) == -1)):
            line = line.strip("\n")
            emaillist = line.split(", ")
            emaillist = list(emaillist)
            email = emaillist[1]
            real_email = email.replace("'", "")
    emaildb.close()
    phonedb = open("phone.txt", "r")
    for line in phonedb:
        if (not (line.find(userid) == -1)):
            line = line.strip("\n")
            phonelist = line.split(", ")
            phonelist = list(phonelist)
            phone = phonelist[1]
            real_phone = phone.replace("'", "")
    phonedb.close()
    genderdb = open("gender.txt", "r")
    for line in genderdb:
        if (not (line.find(userid) == -1)):
            line = line.strip("\n")
            genderlist = line.split(", ")
            genderlist = list(genderlist)
            gender = genderlist[1]
            real_gender = gender.replace("'", "")
    genderdb.close()
    dobdb = open("dob.txt", "r")
    for line in dobdb:
        if (not (line.find(userid) == -1)):
            line = line.strip("\n")
            doblist = line.split(", ")
            doblist = list(doblist)
            dob = doblist[1]
            real_dob = dob.replace("'", "")
    dobdb.close()
    print("Your personal information:")
    print("Your username : " + final_username)
    print("Your E-Mail : " + real_email)
    print("Your phone number : " + real_phone)
    print("Your gender : " + real_gender)
    print("Your date of birth : " + real_dob)
    username="'"+final_username+"'"
    input("Press enter to exit.")
    return user_menu(username, userid)


def user_menu(username, userid):
    while True:
        final_username = username.replace("'", "")
        print("==========================================")
        print("Welcome back! , " + final_username + "!")
        print("==========================================")
        print("Enter 1 to view all or search for specific groceries in the system")
        print("Enter 2 to place an order")
        print("Enter 3 to view your order")
        print("Enter 4 to view your personal information")
        print("Enter 5 to exit")
        login_sys = input("Please enter a number : ")

        if login_sys == "1":
            view_groceries()
        elif login_sys == "2":
            order_groc(username, userid)
        elif login_sys == "3":
            check_order(username, userid)
        elif login_sys == "4":
            cs_info(username, final_username, userid)
        elif login_sys == "5":
            quit()
        else:
            print("\nPlease enter a VALID NUMBER ( 1 ~ 5 ) \n")


def check_order(username, userid):
    print("The items that you bought : ")
    csorderdb = open("csorder.txt", "r")
    for line in csorderdb:
        line = line.strip("\n")
        csorderlist = line.split(", ")
        csorderlist = list(csorderlist)
        if csorderlist[0] == userid:
            listuserid = csorderlist[0]
            item_name = csorderlist[1]
            exp_item = csorderlist[2]
            price_item = csorderlist[3]
            detail_item = csorderlist[4]
            qty_item = csorderlist[5]
            cty_item = csorderlist[6]
            print(
                "Item name : " + item_name + ", Expiry date : " + exp_item + ", Price : " + price_item +
                ", Details : " + detail_item + ", Quantity : " + qty_item + ", Category : " + cty_item + "\n")
    input("Press enter to exit : ")
    username = "'" + username + "'"
    return user_menu(username, userid)


def order_groc(username, userid):
    groceriesdb = open("grocereies.txt", "r")
    line_num = 0
    for line in groceriesdb:
        line = line.strip("\n")
        grocerieslist = line.split(", ")
        grocerieslist = list(grocerieslist)
        item_name = grocerieslist[0]
        exp_item = grocerieslist[1]
        price_item = grocerieslist[2]
        detail_item = grocerieslist[3]
        qty_item = grocerieslist[4]
        cty_item = grocerieslist[5]
        line_num = line_num + 1
        print("No:" + str(
            line_num) + " | Item name : " + item_name + ", Expiry date : " + exp_item + ", Price : " + price_item +
              ", Details : " + detail_item + ", Quantity : " + qty_item + ", Category : " + cty_item + "\n")
    item_select = input("Please choose which item to add in your cart")
    return add_groc(username, item_select, userid)


def add_groc(username, item_select, userid):
    item_select = int(item_select)
    item_select = item_select - 1
    selecteditem = open("grocereies.txt", "r").readlines()[item_select].strip("\n").split(", ")
    selecteditem = list(selecteditem)
    item_name = selecteditem[0]
    exp_item = selecteditem[1]
    price_item = selecteditem[2]
    detail_item = selecteditem[3]
    qty_item = selecteditem[4]
    cty_item = selecteditem[5]
    csorderdb = open("csorder.txt", "a")
    csorder = userid + ", " + item_name + ", " + exp_item + ", " + price_item + ", " + detail_item + ", " + qty_item + ", " + cty_item + "\n"
    csorderdb.write(csorder)
    csorderdb.close()
    username = "'" + username + "'"
    user_menu(username, userid)


def admin_menu():
    while True:
        print("=============================")
        print("=    ADMINISTRATOR MODE     =")
        print("=============================")
        print("Enter 1 to upload groceries details into the system.")
        print("Enter 2 to view all or search for specific groceries in the system")
        print("Enter 3 to update or delete existing groceries detail in the system")
        print("Enter 4 to view all orders of customers.")
        print("Enter 5 to exit")
        login_sys = input("Please enter a number : ")

        if login_sys == "1":
            groceries_sys()
        elif login_sys == "2":
            view_groceries()
        elif login_sys == "3":
            mod_groceries()
        elif login_sys == "4":
            viewallcs()
        elif login_sys == "5":
            quit()
        else:
            print("\nPlease enter a VALID NUMBER ( 1 ~ 5 ) \n")

def viewallcs():
    csdb = open("csorder.txt", "r")
    for line in csdb:
        line = line.strip("\n")
        csorderlist = line.split(", ")
        csorderlist = list(csorderlist)
        userid = csorderlist[0]
        item_name = csorderlist[1]
        exp_item = csorderlist[2]
        price_item = csorderlist[3]
        detail_item = csorderlist[4]
        qty_item = csorderlist[5]
        cty_item = csorderlist[6]
        usernamedb = open("username.txt", "r")
        for line in usernamedb:
            line = line.strip("\n")
            usernamelist = line.split(", ")
            usernamelist = list(usernamelist)
            usernameid = usernamelist[0]
            if usernameid == userid:
                username = usernamelist[1]
        username = username.replace("'", "")
        print("User : "+username+", Item name : " + item_name + ", Expiry date : " + exp_item + ", Price : "
              + price_item + ", Details : " + detail_item + ", Quantity : " + qty_item + ", Category : " + cty_item + "\n")
    input("Press any key to exit.")
    return

def groceries_sys():
    print("Do you want to upload new groceries detail into the system?")
    cfm = input("1. Yes\n2. No :")
    if cfm == "1":
        groceriesdb = open("grocereies.txt", "a")
        item_name = input("Enter the name of the product : ")
        exp_item = input("Enter the expiry date of the product (If available) : ")
        price_item = input("Enter the price of the product : ")
        detail_item = input("Enter the specification of this product (If available) :")
        qty_item = input("Enter the amount of this item available : ")
        cty_item = input("Give item a specific category : ")
        groceriesdb.write(item_name + ", " + exp_item + ", " + price_item + ", " + detail_item + ", " + qty_item + ", " + cty_item + "\n")
        groceriesdb.close()
        print("Returning to last page...")
        return groceries_sys()
    elif cfm == "2":
        return admin_menu()
    else:
        print("Please enter a VALID number!:")
        return groceries_sys()

def new_data_proc(line_cfm):
    line_cfm = line_cfm - 1
    groceriesdb = open("grocereies.txt", "r")
    selecteditem = open("grocereies.txt", "r").readlines()[line_cfm].strip("\n").split(", ")
    selecteditem = list(selecteditem)
    groceriesdb.close()
    return selecteditem

def new_data(line_cfm):
    line_cfm = int(line_cfm)
    print("Which specific variable you want to edit?")
    cfm = input(
        "1. Item name\n2. Expiry Date\n3. Price\n4. Details\n5. Quantity\n6. Category\n7. Delete \n8. Exit \nChoose an number : ")
    if cfm == "1":
        new_input = input("Please enter your new item name : ")
        selecteditem=new_data_proc(line_cfm)
        exp_item = selecteditem[1]
        price_item = selecteditem[2]
        detail_item = selecteditem[3]
        qty_item = selecteditem[4]
        cty_item = selecteditem[5]
        newData = new_input + ", " + exp_item + ", " + price_item + ", " + detail_item + ", " + qty_item + ", " + cty_item + "\n"
        return newData
    elif cfm == "2":
        new_input = input("Please enter your new expiry date: ")
        selecteditem=new_data_proc(line_cfm)
        item_name = selecteditem[0]
        price_item = selecteditem[2]
        detail_item = selecteditem[3]
        qty_item = selecteditem[4]
        cty_item = selecteditem[5]
        newData = item_name + ", " + new_input + ", " + price_item + ", " + detail_item + ", " + qty_item + ", " + cty_item + "\n"
        return newData
    elif cfm == "3":
        new_input = input("Please enter your new pricing : ")
        selecteditem=new_data_proc(line_cfm)
        item_name = selecteditem[0]
        exp_item = selecteditem[1]
        detail_item = selecteditem[3]
        qty_item = selecteditem[4]
        cty_item = selecteditem[5]
        newData = item_name + ", " + exp_item + ", " + new_input + ", " + detail_item + ", " + qty_item + ", " + cty_item + "\n"
        return newData
    elif cfm == "4":
        new_input = input("Please enter your new item specification : ")
        selecteditem=new_data_proc(line_cfm)
        item_name = selecteditem[0]
        exp_item = selecteditem[1]
        price_item = selecteditem[2]
        detail_item = selecteditem[3]
        qty_item = selecteditem[4]
        cty_item = selecteditem[5]
        newData = item_name + ", " + exp_item + ", " + price_item + ", " + new_input + ", " + qty_item + ", " + cty_item + "\n"
        return newData
    elif cfm == "5":
        new_input = input("Please enter your new item quantity : ")
        selecteditem=new_data_proc(line_cfm)
        item_name = selecteditem[0]
        exp_item = selecteditem[1]
        price_item = selecteditem[2]
        detail_item = selecteditem[3]
        cty_item = selecteditem[5]
        newData = item_name + ", " + exp_item + ", " + price_item + ", " + detail_item + ", " + new_input + ", " + cty_item + "\n"
        return newData
    elif cfm == "6":
        new_input = input("Please enter your new item category : ")
        selecteditem=new_data_proc(line_cfm)
        item_name = selecteditem[0]
        exp_item = selecteditem[1]
        price_item = selecteditem[2]
        detail_item = selecteditem[3]
        qty_item = selecteditem[4]
        newData = item_name + ", " + exp_item + ", " + price_item + ", " + detail_item + ", " + qty_item + ", " + new_input + "\n"
        return newData
    elif cfm == "7":
        print("Are you really sure you want to delete this list?")
        del_cfm = input("Type 1 to delete\nType 2 to cancel : ")
        if del_cfm == "1":
            selecteditem=new_data_proc(line_cfm)
            newData = ""
            return newData
        elif del_cfm == "2":
            return new_data(line_cfm)
        else:
            print("Please enter a VALID number!")
            return new_data(line_cfm)
    elif cfm == "8":
        return admin_menu()
    else:
        print("Please enter a VALID number!")
        return new_data(line_cfm)


def mod_groceries_list(line_cfm):
    groceriesdb = open("grocereies.txt", "r")
    lineCount = 1
    for line in groceriesdb:
        if (lineCount == int(line_cfm)):
            groceriesdb = open("grocereies.txt", "r")
            groceriesData = groceriesdb.read()
            oldData = line
            newData = new_data(line_cfm)
            groceriesData = groceriesData.replace(oldData, newData)
        lineCount += 1
    groceriesdb = open("grocereies.txt", "w")
    groceriesdb.write(groceriesData)
    groceriesdb.close()
    return mod_groceries()


def mod_groceries():
    groceriesdb = open("grocereies.txt", "r")
    line_num = 0
    for line in groceriesdb:
        line = line.strip("\n")
        grocerieslist = line.split(", ")
        grocerieslist = list(grocerieslist)
        item_name = grocerieslist[0]
        exp_item = grocerieslist[1]
        price_item = grocerieslist[2]
        detail_item = grocerieslist[3]
        qty_item = grocerieslist[4]
        cty_item = grocerieslist[5]
        line_num = line_num + 1
        print("No:" + str(
            line_num) + " | Item name : " + item_name + ", Expiry date : " + exp_item + ", Price : " + price_item +
              ", Details : " + detail_item + ", Quantity : " + qty_item + ", Category : " + cty_item + "\n")
    line_cfm = input("Which item would you like to make changes on? Or type E to exit : ")
    line_cfm = line_cfm.lower()
    if line_cfm == "e":
        admin_menu()
    return mod_groceries_list(line_cfm)

def view_groceries():
    print("\nHow would you like to view the existing groceries details?")
    print("1. View all groceries from the oldest date "
          "till the latest date that an item has added to the system\n"
          "2. View groceries by category\n"
          "3. Exit\n")
    cfm = input("Type 1 or 2 or 3 to proceed : ")
    if cfm == "1":
        groceriesdb = open("grocereies.txt", "r")
        for line in groceriesdb:
            line = line.strip("\n")
            grocerieslist = line.split(", ")
            grocerieslist = list(grocerieslist)
            item_name = grocerieslist[0]
            exp_item = grocerieslist[1]
            price_item = grocerieslist[2]
            detail_item = grocerieslist[3]
            qty_item = grocerieslist[4]
            cty_item = grocerieslist[5]
            print(
                "Item name : " + item_name + ", Expiry date : " + exp_item + ", Price : "
                + price_item + ", Details : " + detail_item + ", Quantity : " + qty_item + ", Category : " + cty_item + "\n")
        cfm_exit = input("Press any key to exit.")
        groceriesdb.close()
        return view_groceries()
    elif cfm == "2":
        print("Choose which category would you like to find?")
        cty_cfm = input(" 1. Toys\n 2. Foods\n 3. Drinks\n 4. Supplements\nType a number to proceed : ")
        if cty_cfm == "1":
            cty_slt = "Toys"
            groceriesdb = open("grocereies.txt", "r")
            for line in groceriesdb:
                if (not (line.find(cty_slt) == -1)):
                    line = line.strip("\n")
                    grocerieslist = line.split(", ")
                    grocerieslist = list(grocerieslist)
                    item_name = grocerieslist[0]
                    exp_item = grocerieslist[1]
                    price_item = grocerieslist[2]
                    detail_item = grocerieslist[3]
                    qty_item = grocerieslist[4]
                    cty_item = grocerieslist[5]
                    print(
                        "Item name : " + item_name + ", Expiry date : " + exp_item + ", Price : " + price_item +
                        ", Details : " + detail_item + ", Quantity : " + qty_item + ", Category : " + cty_item + "\n")
            cfm_exit = input(
                "If there are no items shown, it means there are no " + cty_slt + " keyword related items, Press any key to exit.")
            groceriesdb.close()
            return view_groceries()
        elif cty_cfm == "2":
            cty_slt = "Foods"
            groceriesdb = open("grocereies.txt", "r")
            for line in groceriesdb:
                if (not (line.find(cty_slt) == -1)):
                    line = line.strip("\n")
                    grocerieslist = line.split(", ")
                    grocerieslist = list(grocerieslist)
                    item_name = grocerieslist[0]
                    exp_item = grocerieslist[1]
                    price_item = grocerieslist[2]
                    detail_item = grocerieslist[3]
                    qty_item = grocerieslist[4]
                    cty_item = grocerieslist[5]
                    print(
                        "Item name : " + item_name + ", Expiry date : " + exp_item + ", Price : " + price_item + ", Details : " + detail_item + ", Quantity : " + qty_item + ", Category : " + cty_item + "\n")
            cfm_exit = input(
                "If there are no items shown, it means there are no " + cty_slt + " keyword related items, Press any key to exit.")
            groceriesdb.close()
            return view_groceries()
        elif cty_cfm == "3":
            cty_slt = "Drinks"
            groceriesdb = open("grocereies.txt", "r")
            for line in groceriesdb:
                if (not (line.find(cty_slt) == -1)):
                    line = line.strip("\n")
                    grocerieslist = line.split(", ")
                    grocerieslist = list(grocerieslist)
                    item_name = grocerieslist[0]
                    exp_item = grocerieslist[1]
                    price_item = grocerieslist[2]
                    detail_item = grocerieslist[3]
                    qty_item = grocerieslist[4]
                    cty_item = grocerieslist[5]
                    print(
                        "Item name : " + item_name + ", Expiry date : " + exp_item + ", Price : " + price_item + ", Details : " + detail_item + ", Quantity : " + qty_item + ", Category : " + cty_item + "\n")
            cfm_exit = input("Press any key to exit.")
            groceriesdb.close()
            return view_groceries()
        elif cty_cfm == "4":
            cty_slt = "Supplements"
            groceriesdb = open("grocereies.txt", "r")
            for line in groceriesdb:
                if (not (line.find(cty_slt) == -1)):
                    line = line.strip("\n")
                    grocerieslist = line.split(", ")
                    grocerieslist = list(grocerieslist)
                    item_name = grocerieslist[0]
                    exp_item = grocerieslist[1]
                    price_item = grocerieslist[2]
                    detail_item = grocerieslist[3]
                    qty_item = grocerieslist[4]
                    cty_item = grocerieslist[5]
                    print(
                        "Item name : " + item_name + ", Expiry date : " + exp_item + ", Price : " + price_item + ", Details : " + detail_item + ", Quantity : " + qty_item + ", Category : " + cty_item + "\n")
            cfm_exit = input("Press any key to exit.")
            groceriesdb.close()
            return view_groceries()
        else:
            print("Please enter a VALID number!")
    elif cfm == "3":
        return
    else:
        print("Please enter a VALID number! ( 1 ~ 3 )")
        return view_groceries()


def login_menu():
    username = input("Please enter your username : ")
    username = "'" + username + "'"
    usernamedb = open("username.txt", "r")
    for line in usernamedb:
        if not (line.find(username) == -1):
            line = line.strip("\n")
            usernamelist = line.split(", ")
            usernamelist = list(usernamelist)
            userid = usernamelist[0]
            password = input("Please enter your password to login : ")
            password = "'" + password + "'"
            passworddb = open("password.txt", "r")
            for line in passworddb:
                if not (line.find(userid) == -1):
                    line = line.strip("\n")
                    passwordlist = line.split(", ")
                    passwordlist = list(passwordlist)
                    passworddata = passwordlist[1]
                    if passworddata == password:
                        print("You have logged in!\n")
                        return user_admin_check(userid, username)
                    else:
                        print("You entered the wrong password fool!")
                        return login_menu()
    print("There are no existing members registered in this system.")
    print("Returning to main menu...")
    return mainmenu()


def login_decision():
    print("Welcome back!, Please login to have user access.")
    logm_choice = input("Type 1 to proceed to login \nType 2 to return to main menu : ")
    if logm_choice == "1":
        return login_menu()
    elif logm_choice == "2":
        return mainmenu()
    else:
        print("\nPlease inside a valid number!\n")
        return login_decision()


def register_menu():
    print("We welcome you to be a part of our customer!")
    print("Please fill in the required information in order to proceed!")
    username_sec()
    password_sec()
    email_sec()
    phone_sec()
    gender_sec()
    dob_sec()
    print("Your registration has been succeeded, please choose 1. in main menu in order to login.")
    print("Returning to main menu...")
    return mainmenu()

def username_check():
    username = input("Please enter your username : ").lower()
    usernamedb = open("username.txt", "r")
    for line in usernamedb:
        line = line.strip("\n")
        usernamelist = line.split(", ")
        usernamelist = list(usernamelist)
        usernamedata = usernamelist[1]
        usernamedata = usernamedata.replace("'", "")
        if usernamedata == username:
            print("The username has been taken, please try another username!")
            usernamedb.close()
            return 0
    usernamedb.close()
    return username

def username_sec():
    lineuserid = 1
    username = username_check()
    if username == 0:
        return username_sec()
    if len(username) > 15:
        print("Your username has exceeded the system limit, please try again!")
        return username_sec()
    elif len(username) < 8:
        print("Your username is too short, please try again!")
        return username_sec()
    elif (username == "admin"):
        print("This username has been used by our internal system, please try another username!")
        return username_sec()
    else:
        username = "'" + username + "'"
        usernamedb = open("username.txt", "r")
        for line in usernamedb:
            lineuserid += 1
        userid = lineuserid
        userid = str(userid)
        usernamedb = open("username.txt", "a")
        usernamedb.write(userid + ", " + username + "\n")
        usernamedb.close()


def password_sec():
    linepassid = 1
    passworddb = open("password.txt", "r")
    password = input("Please enter your password : ")
    if len(password) > 10 & len(password) < 8:
        print("Your password is not within the required length, ( Minimum 8 characters up to 10 )")
        return password_sec()
    confirmpassword = input("Please re-enter your password to confirm : ")
    if (not ((password) == (confirmpassword))):
        print("The password is not the same as you type, please try again!")
        return password_sec()
    else:
        password = "'" + password + "'"
        for line in passworddb:
            linepassid += 1
        userid = linepassid
        userid = str(userid)
        passworddb = open("password.txt", "a")
        passworddb.write(userid + ", " + password + "\n")
        passworddb.close()


def email_sec():
    lineemailid = 1
    emaildb = open("email.txt", "r")
    email = input("Please enter your email address : ")
    if (email.find("@") == -1):
        print("Please enter a VALID email address! e.g : xxxx@mail.com")
        return email_sec()
    else:
        email = "'" + email + "'"
        for line in emaildb:
            lineemailid += 1
        userid = lineemailid
        userid = str(userid)
        emaildb = open("email.txt", "a")
        emaildb.write(userid + ", " + email + "\n")
        emaildb.close()


def phone_sec():
    linephoneid = 1
    phonedb = open("phone.txt", "r")
    phone = input("Please enter your phone number : ")
    try:
        int(phone)
    except:
        print("Please enter a VALID phone number! Numbers only!")
        return phone_sec()
    if len(phone) < 10 or int(phone) < 0 or len(phone) > 11:
        print("Please enter a VALID phone number! It's should contain 10 to 11 numbers!")
        return phone_sec()
    else:
        phone = "'" + phone + "'"
        for line in phonedb:
            linephoneid += 1
        userid = linephoneid
        userid = str(userid)
        phonedb = open("phone.txt", "a")
        phonedb.write(userid + ", " + phone + "\n")
        phonedb.close()


def gender_sec():
    linegenderid = 1
    genderdb = open("gender.txt", "r")
    gender = input("Please type your gender : \n1. Male \n2. Female \n3. Others\n")
    if gender == "1":
        genderinfo = "Male"
    elif gender == "2":
        genderinfo = "Female"
    elif gender == "3":
        genderinfo = "Others"
    else:
        print("Enter a VALID number! ( 1 ~ 3 )")
        return gender_sec()
    genderinfo = "'" + genderinfo + "'"
    for line in genderdb:
        linegenderid += 1
    userid = linegenderid
    userid = str(userid)
    genderdb = open("gender.txt", "a")
    genderdb.write(userid + ", " + genderinfo + "\n")
    genderdb.close()


def dob_sec():
    linedobid = 1
    dobdb = open("dob.txt", "r")
    dob = input("Please type your date of birth (DD/MM/YYYY) : ")
    dob = "'" + dob + "'"
    for line in dobdb:
        linedobid += 1
    userid = linedobid
    userid = str(userid)
    dobdb = open("dob.txt", "a")
    dobdb.write(userid + ", " + dob + "\n")
    dobdb.close()


def mainmenu():
    while True:
        print("================================================")
        print("=  Welcome to FRESHCO Online Groceries Store!  =")
        print("================================================")
        print("Enter 1 to login for existing customers")
        print("Enter 2 for new customers")
        print("Enter 3 to exit")
        login_sys = input("Please enter a number : ")

        if login_sys == "1":
            login_decision()
        elif login_sys == "2":
            register_menu()
        elif login_sys == "3":
            quit()
        else:
            print("\nPlease enter a VALID NUMBER ( 1 ~ 4 ) \n")


# The main code starts here:
mainmenu()
