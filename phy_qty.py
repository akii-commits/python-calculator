import math
print("calculate physical quantity ")
print("A  - area")
print("C  - cirumference")
print("V  - volume")


mode=input("Select quantity : ")

if mode=='D' or mode=='d':
    print("Density calculator")
elif mode=="A" or mode=="a":
    print("area calaculator")

elif mode=="C" or mode=="c":
    print("circumference calaculator")

elif mode=="V" or mode=="v":
    print("volume calaculator")

elif mode=="At" or mode=="at"or mode=="AT":
    print("accelaration calaculator")

elif mode=="U" or mode=="u":
    print("Velocity calaculator")

else:
    print("Invalid key")
    print("try again")


#area calculator
print()
print("\nR - rectangle")
print("S - square")
print("C - cirlcle")
print("P - paralleogram")
print("T - triangle")

shape=input("select shape : ")

if shape=="R" or shape=="r":
    print("Rectangle selected")
    width=int(input("Enter width : "))
    lenght=int(input("Enter legth :"))
    print(width*lenght,"cm")

elif shape=="S" or shape=="s":
    print("Square selcted")
    side=int(input("Enter lenght : "))
    print(side*side,"cm")

elif shape=="C" or shape=="c":
    print("circle selcted")
    radius=int(input("Enter radius : "))
    print(3.14*radius^2,"cm")


elif shape=="P" or shape=="p":
    print("Parallogram selected")
    height=int(input("Enter height : "))
    base=int(input("Enter base"))
    print(base*height,"cm")

elif shape=="T" or shape=="t":
    print("Triangle selcted")
    height=int(input("Enter height : "))
    base=int(input("Enter base"))
    print(0.5*base*height,"cm")
else:
    print("Invalid key")
    print("try again")

#circumference calculator
print()
print("\nR - rectangle")
print("S - square")
print("C - cirlcle")
print("P - paralleogram")
print("T - triangle")

shape=input("select shape : ")

if shape=="R" or shape=="r":
    print("Rectangle selected")
    width=int(input("Enter width : "))
    lenght=int(input("Enter legth :"))
    print(2*(width+lenght),"cm")

elif shape=="S" or shape=="s":
    print("Square selcted")
    side=int(input("Enter lenght : "))
    print(4*side,"cm")

elif shape=="C" or shape=="c":
    print("circle selcted")
    radius=int(input("Enter radius : "))
    print(2*3.14*radius,"cm")


elif shape=="P" or shape=="p":
    print("Parallogram selected")
    p_widht=int(input("Enter height : "))
    p_lenght=int(input("Enter base"))
    print(2*(p_lenght+p_widht),"cm")

elif shape=="T" or shape=="t":
    print("Triangle selcted")
    height=int(input("Enter height : "))
    base=int(input("Enter base"))
    print(0.5*base*height,"cm")
else:
    print("Invalid key")
    print("try again")

#vloume calculator
print()
print("\nR - rectangle")
print("S - square")
print("C - cirlcle")
print("P - paralleogram")
print("T - triangle")

shape=input("select shape : ")

if shape=="R" or shape=="r":
    print("Rectangle selected")
    width=int(input("Enter width : "))
    lenght=int(input("Enter legth :"))
    print(width*lenght,"cm")

elif shape=="S" or shape=="s":
    print("Square selcted")
    side=int(input("Enter lenght : "))
    print(side*side,"cm")

elif shape=="C" or shape=="c":
    print("circle selcted")
    radius=int(input("Enter radius : "))
    print(2*3.14*radius,"cm")


elif shape=="P" or shape=="p":
    print("Parallogram selected")
    height=int(input("Enter height : "))
    base=int(input("Enter base"))
    print(base*height,"cm")

elif shape=="T" or shape=="t":
    print("Triangle selcted")
    height=int(input("Enter height : "))
    base=int(input("Enter base"))
    print(0.5*base*height,"cm")
else:
    print("Invalid key")
    print("try again")