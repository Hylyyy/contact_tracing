print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

#DISPLAY A MENU.

def menu():
    
    print("\t||-||-||- MENU - ||-||-||")
    print("\t||                     ||")
    print("\t||   1. Add an item    ||")
    print("\t||   2. Search         ||")
    print("\t||   3. Exit           ||")
    print("\t||                     ||")
    print("\t||-||-||-||-|-||-||-||-||")
    print()

menu()

#DICTIONARY

contact_info = {}

#ASK THE USER TO SELECT AN ITEM IN THE MENU.
while True:
    option = int(input("Please choose an option: "))
    print()

#PERFORMING THE SELECTED OPTION.
#IF OPTION 1 IS CHOSEN: the user will be ask for his/her personal data.

    if option == 1:
        print("========CONTACT INFORMATION========")
        print()
        name = input("What is your full name?: ")
        address = input("Please enter your address: ")
        age = input("What is your age?: ")
        phone_num = input("What is your phone number: ")
        gender = input("What is your Gender?: ")
        blood_type = input("What is your blood type?: ")
        body_temp = input("What is your body temperature?: ")
        vacc_status = input("Are you fully vaccinated?: ")
        contact_info[name] = {"Address":address, "Age": age, "Phone number": phone_num, "Gender":gender, "Blood type": blood_type, 
        "Body Temperature": body_temp, "Vaccination": vacc_status} 
        print()
        print("===================================")
        print()
        
        menu()

    #IF OPTION 2: the user will try to search using the full name.
    elif option == 2:
        print("===============Search==============")
        print("      Here are the result/s:")
        print("===================================")
        print()
        search = input("Enter the full name: ")
        for i, x in contact_info[search].items():
            print(i,":",x)
        print("===================================")
        print()
        menu()

    # IF OPTION 3: the user will be ask if he/she wants to exit the program. 

    elif option == 3:
        print("===================================")
        exit = input("\nDo you want to exit? (y/n): ")
        print()
        if exit == "n" or exit == "N":
            menu()
        else:
            print("=====Thank you for using me!!!=====")
            break
