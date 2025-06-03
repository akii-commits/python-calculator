print("What oppretion would you like to choose?")
print()
print("=========OPERATIONS=========")
print(" trignometric ratios")
print("logarithmic ")
print("Factorial ")
print("gif function ")
print("Exponential")
print()
print()
input("Press enter to coninue")

def menu():
    print("======================")
    print("SELECT CALCULATOR MODES")
    print("======================")
    print("press 1 'Basic'")
    print("press 2 'Scientific'")
    print("press 3 'Quantity'")
    print("press 4 'Menstruation'")
    print("======================")
    print()

def mode():
    ch1=int(input("Press the key:"))
    if ch1==1:
        print("Basic Mode selected...")
    elif ch1==2:
        print("scientific mode selected...")
    elif ch1==3:
        print("Quantity mode selected...")
    elif ch1==4:
        print("Menstruation mode selected...")
    else:      #value error occurs code crashes when any other key is inputed than a integer in mode() 
                #to be fixed later....
        print()
        print("======================")
        print("***Invalid key***")    
        print("======================")
        print()
        mode()

menu()
mode()