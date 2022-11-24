import time
import os

name_list = []
contact_list = []

while(True):
    print("\n     ---------------     1. Add a New Contact        ---------------\n")
    print("     ---------------     2. View a Contact           ---------------\n")
    print("     ---------------     3. Display all Contacts     ---------------\n")
    print("     ---------------     0. Exit                     ---------------\n")
    choice = int(input("Enter Your Choice: "))
    time.sleep(0.25)
    os.system('cls')
    if(choice == 1):
        name = str(input("     Enter The Name    \n\t"))
        contact = int(input("     Enter Contact Number     \n\t"))
        name_list.append(name)
        contact_list.append(contact)
        os.system('cls')
    elif(choice == 2):
        print("\n     ---------------     1. Search by Name        ---------------\n")
        print("     ---------------     0. Search by Contact     ---------------\n")
        usr_choice = int(input("Enter Your Choice: "))
        time.sleep(0.25)
        os.system('cls')
        if(usr_choice == 1):
            name = str(input("      Enter the Name of Contact You want to Search     \n\t"))
            if(name in  name_list):
                index = name_list.index(name)
                os.system('cls')
                print("---     ", name_list[index], " : ", contact_list[index], "     ---\n")
                time.sleep(1)
                os.system('cls')
            else:
                os.system('cls')
                print("\n     --------------     Sorry, Name Not Found     ---------------\n")
                time.sleep(0.25)
                os.system('cls')
        elif(usr_choice == 0):
            contact = int(input("      Enter the Name of Contact You want to Search     \n\t"))
            if(contact in  contact_list):
                index = contact_list.index(contact)
                os.system('cls')
                print("---     ", name_list[index], " : ", contact_list[index], "     ---\n")
                time.sleep(1)
                os.system('cls')
            else:
                os.system('cls')
                print("\n     --------------     Sorry, Contact Not Found     ---------------\n")
                time.sleep(0.25)
                os.system('cls')
        else:
            os.system('cls')
            print("\n     ---------------     INVALID  CHOICE     ---------------\n")
            time.sleep(0.25)
            os.system('cls')
    elif(choice == 3):
        print("\n     ---------------     Contacts     ----------------\n")
        for index in range(0, len(name_list)):
            print("---     ", name_list[index], " : ", contact_list[index], "     ---\n")
            time.sleep(1)
    elif(choice == 0):
        print("\n     ---------------     Thanks For Using Our Software!!!     ---------------\n")
        break
    else:
        os.system('cls')
        print("\n     ---------------     INVALID  CHOICE     ---------------\n")
        time.sleep(0.25)
        os.system('cls')
        print("\n     ---------------     RESTARTING.........     ---------------\n")
        time.sleep(0.25)
        os.system('cls')
