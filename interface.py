#import quick_list, live_list
cont = True #to keep program running unless explicity ended by input
print("***************************")                    
print("Welcome to this Automated Shopping List Program")


while(cont):
    print("Main Menu")
    print("***************************")
    print("Enter 1 for Quick List")
    print("Enter 2 for Personalised List")
    print("Enter 3 to enter a reciept to the CSV")
    print("Enter 4 for Edit CSV menu")
    print("Enter 5 for Help Information")
    print("***************************")
    print("Enter 'End' while in the main menu to terminate program")
    print("***************************")

    selection = input()
    if(selection.casefold() == "End".casefold()): #.casefold() == java's compareToIgnoreCase()
        cont = False

    if(selection == "1"):
        print("***************************")
        import quick_list
    if(selection == "2"):
        print("***************************")
        import live_list

print("*************")
print("Program Terminated")
print("*************")

