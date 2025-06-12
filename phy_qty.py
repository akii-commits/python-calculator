import math

def msg():
    msg=input("\ndo you want to continue (y/n) :").lower()
    return msg == "y"
    


        
#volume calculator

def volume_cal():
    print ("\n==== Select shape ===")
    print ("S  - Sphere")
    print ("C  - cuboid")
    print ("cl - Cylinder")
    print ("P  - prism")
    print ("cu - cube")
    print ("py - pyramid")
    print ("\nE  - Exit")
    vshape=input("\nEnter shape :").lower()
    if vshape == "s":
        while True:
            print ("\nH - Hollow Sphere")        
            print ("S - solid sphere")
            print ("\nE - exit")
            sphere=input("\nselect sphere :").lower()
            if sphere=="h":
                rad = int(input("\nEnter radius :"))
                result = 4/3*(3.14*pow(rad,3))
                print(result,"cm")
                if not msg():
                    break
    
    elif vshape == "c":
        while True:
            print("\n=== Cuboid selected ===")
            lenght = int(input("\nEnter lenght :"))
            breath = int(input("Enter breadth :"))
            height = int(input("Enter height : "))
            print(lenght*breath*height,"cm")
            if not msg():
                break
    
    elif vshape == "cl":
        while True:
            print("\n=== cylinder selected ===")
            h = int(input("\nEnter height : "))
            r = int(input("Enter radius : "))
            print(3.14*pow(r,2)*h,"cm")
            if not msg():
                break
    
    elif vshape == "cu":
        while True:
            print("\n=== cube selected ===")
            a = int(input("\nEnter leght of any side :"))
            print(pow(a,3),"cm")
            if not msg():
                break

    elif vshape == "py":
        while True:
            print("\n=== Pyramid selected ===")
            print("\nTo calculate base area press 0")
            a = int(input("Enter base area : "))
            if a == 0:
                height=int(input("\nEnter height : "))
                base=int(input("Enter base"))
                result = 0.5*base*height
                print(result,"cm")
                a = result
                h = int(input("Enter height : "))
                print(1/3*a*h,"cm")
                if not msg():
                    break
            else:
                h = int(input("Enter height : "))
                print(1/3*a*h,"cm")
                if not msg():
                    break

    else:
        print("Invalid input, try again")
        return volume_cal()

                


#area calculator
def area_cal():
    while True:
        print("\nR - rectangle")
        print("S - square")
        print("C - cirlcle")
        print("P - paralleogram")
        print("T - triangle")
        print("\nB - back")

        shape=input("\nselect shape : ").lower()

        if shape=="r":
            while True:
                print("Rectangle selected")
                width=int(input("\nEnter width : "))
                lenght=int(input("Enter legth :"))
                print(width*lenght,"cm")
                if not msg():
                    break 

        elif shape=="s":
            while True:
                print("Square selcted")
                side=int(input("\nEnter lenght : "))
                print(side*side,"cm")
                if not msg():
                    break 

        elif shape=="c":
            while True:
                print("circle selcted")
                radius=int(input("\nEnter radius : "))
                print(3.14*radius**2,"cm")
                if not msg():
                    break 

        elif shape=="p":
            while True:
                print("Parallogram selected")
                height=int(input("\nEnter height : "))
                base=int(input("Enter base"))
                print(base*height,"cm")
                if not msg():
                    break 

        elif shape=="t":
            while True:
                print("Triangle selcted")
                height=int(input("\nEnter height : "))
                base=int(input("Enter base"))
                print(0.5*base*height,"cm")
                if not msg():
                    break 
        elif shape == "b":
            break

        else:
            print("Invalid key")
            print("try again")

#circumference calculator
def p_cal():
    while True:
        print("\nR - rectangle")
        print("S - square")
        print("C - cirlcle")
        print("P - paralleogram")
        print("T - triangle")
        print("B - back")

        shape=input("\nselect shape : ").lower()

        if shape=="r":
            print("\n=== Rectangle selected ===")
            width=int(input("\nEnter width : "))
            lenght=int(input("Enter legth :"))
            print(2*(width+lenght),"cm")
            if not msg():
                break

        elif shape=="s":
            print("\n=== Square selcted ===")
            side=int(input("\nEnter lenght : "))
            print(4*side,"cm")
            if not msg():
                break

        elif shape=="c":
            print("\n=== circle selcted ===")
            radius=int(input("\nEnter radius : "))
            print(2*3.14*radius,"cm")
            if not msg():
                break


        elif shape=="p":
            print("\n=== Parallogram selected ===")
            p_widht=int(input("\nEnter height : "))
            p_lenght=int(input("Enter base"))
            print(2*(p_lenght+p_widht),"cm")

        elif shape=="T" or shape=="t":
            print("\n=== Triangle selcted ===")
            height=int(input("\nEnter height : "))
            base=int(input("Enter base"))
            print(0.5*base*height,"cm")

        else:
            print("Invalid key,try again")

    #main menu

while True:    
    print("calculate physical quantity ")
    print("V  - volume")
    print("A  - area")
    print("p  - perimetre")
    print("E  - Exit")


    mode=input("Select quantity : ").lower()

   
    if mode=="a":
        print("\narea calaculator")
        area_cal()

    elif mode=="p":
        print("\nperimetere calaculator")
        p_cal()

    elif mode=="v":
        print("\nvolume calaculator")
        volume_cal()

    elif mode=="e":
        print("\nExiting programe....")
        break

    else:
        print("Invalid key")
        print("\ntry again...")
        