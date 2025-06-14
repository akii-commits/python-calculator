import math

def basic():
    sop=[]
    l=[]
    l2=[]
    data=input("Enter The Expression:") #a+b-4
    a=data
    for d in data:
        if d in "+-*/":
            sop.append(d)

    for i in data:
        if i in "+-*/":
            data=data.replace(i,",")
    new=data.split(",")
   
    l.append(a)

    for s in new:
        if s.isalpha()==True:
            try:
                num=int(s)
            except:
                ValueError
            print("INVAILD EXPRESSION")
            break
        elif s.isalpha()==False:
            num=int(s)
            l2.append(num)

    print("NO of / operators in expression",sop.count("/"))


    ix=-1
    for m in a:
        if m in "+-*/":
            ix+=2
            l2.insert(ix,m)
        
    for i in range(sop.count("/")):
        for n in l2:
            if n=="/": #45+4/2/2
                x=l2.index(n)
                ans=l2[x-1]/l2[x+1]
                l2[x]=ans
                l2.pop(x+1)
                l2.pop(x-1)


    for i in range(sop.count("*")):
        for n in l2:
            if n=="*": #45+4/2/2
                x=l2.index(n)
                ans=l2[x-1]*l2[x+1]
                l2[x]=ans
                l2.pop(x+1)
                l2.pop(x-1)


    for i in range(sop.count("+")):
        for n in l2:
            if n=="+": #45+4/2/2
                x=l2.index(n)
                ans=l2[x-1]+l2[x+1]
                l2[x]=ans
                l2.pop(x+1)
                l2.pop(x-1)


    for i in range(sop.count("-")):
        for n in l2:
            if n=="-": #45+4/2/2
                x=l2.index(n)
                ans=l2[x-1]-l2[x+1]
                l2[x]=ans
                l2.pop(x+1)
                l2.pop(x-1)
    
    print("Extracted numbers as string",l)
    print("user data:",a)
    print("numbers",l2)
    print(data)
    print(type(l2[0]))


    
    print(ans)
    print(type(ans))
    print(sop)
    print()
    print()


    def msg():
        print("Do you want to continue?")
        choice=input("'yes'/'no':")
        if choice=="no":
            print()
            print("Returning to main menu...")
            print("SELECT THE MODE")
            #mode() #mode() is not defined merge this to main menu 
        elif choice=="yes":
            print("basic mode continues..")
            basic()
        else:
            print("***Invalid key***")
            msg()
    msg()        

def mensuration():

    def msg():
        while True:
            msg=input("\ndo you want to continue (y/n) :").lower()
            if msg == 'y':
                return msg == "y"
            elif msg == 'n':
                return False
            else:
                print("Invalid input, Try again...")
            
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
                if sphere == "h":
                    rad = int(input("\nEnter radius :"))
                    result = 4/3*(3.14*pow(rad,3))
                    print(result,"cm")
                    if not msg():
                        break
                elif sphere == 's':
                    print("not available yet")
                    break
                elif sphere == 'e':
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
  
            elif shape == 'b':
                break

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
        

def scientific():
    def msg():
        while True:
            msg=input("\ndo you want to continue (y/n) :").lower()
            if msg == 'y':
                return msg == "y"
            elif msg == 'n':
                return False
            else:
                print("Invalid input, Try again...")
            

    def factorial(n):
        if n==1 or n==0:
            return 1 
        else:
            return n*factorial(n-1)
        
    def gif(n):
        b=int(n)
        if n>b:
            return b+1
        else:
            return b
        
    def get_trig_value():
        print("\nEnter trigonometric ratio (sin, cos, tan, sec, cosec, cot):")
        tr = input("Ratio: ").lower()
        if tr in ['sin', 'cos', 'tan', 'sec', 'cosec', 'cot']:
            ang = int(input("Enter angle (in degrees): "))
            rd = math.radians(ang)
            result = {
                "sin": math.sin(rd),
                "cos": math.cos(rd),
                "tan": math.tan(rd),
                "sec": 1 / math.cos(rd),
                "cosec": 1 / math.sin(rd),
                "cot": 1 / math.tan(rd),
            }[tr]
            print(f"{tr}({ang}) = {result}")
            return result
        else:
            print("Invalid Input")
            return get_trig_value()

    def get_log_value():
        try:
            num = int(input("Enter number for log: "))
            result = math.log(num)
            print(f"log({num}) = {result}")
            return result
        except ValueError:
            print("Invalid input, try again.")
            return get_log_value()

    def get_operator():
        op = input("Enter operator (+, -, *, /): ")
        if op in '+-*/':
            return op
        else:
            print("Invalid operator")
            return get_operator()

    def operate(a, b, op):
        return {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a / b,
        }[op]

    def calc_loop(history):
        a = get_trig_value()
        op = get_operator()
        b = get_trig_value()
        result = operate(a, b, op)
        print("Result:", result)
        history.append(result)
        while input("Continue? (y/n): ").lower() == 'y':
            op = get_operator()
            b = get_trig_value()
            result = operate(history[-1], b, op)
            print("Result:", result)
            history.append(result)

    def log_loop(history):
        a = get_log_value()
        op = get_operator()
        b = get_log_value()
        result = operate(a, b, op)
        print("Result:", result)
        history.append(result)
        while input("Continue? (y/n): ").lower() == 'y':
            op = get_operator()
            b = get_log_value()
            result = operate(history[-1], b, op)
            print("Result:", result)
            history.append(result)

    def cal_factorial():
        while True:
            print("==== Factorial mode ====")
            n=int(input("\nEnter a number : "))
            print("Factorial = ",factorial(n))
            if not msg():
                break

    def cal_gif():
        while True:
            print("==== Gif mode ====")
            n=float(input("\nEnter a number : "))
            print("GIF = ",gif(n))
            if not msg():
                break

                
    def scmd():
        history = []
        while True:
            print("\n==== Scientific Calculator Menu ====")
            print("T - Trigonometric Operations")
            print("L - Logarithmic Operations")
            print("G - Gif functions")
            print("F - Factorial")
            print("E - Exit")
            choice = input("\nEnter choice: ").lower()

            if choice == 't':
                calc_loop(history)
            elif choice == 'l':
                log_loop(history)
            elif choice == 'f':
                cal_factorial()
            elif choice == 'g':
                cal_gif()
            elif choice == 'e':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")

    if __name__ == "__main__":
        scmd()

while True:
    print("\n======================")
    print("SELECT CALCULATOR MODES")
    print("======================")
    print("press 1 'Basic'")
    print("press 2 'Scientific'")
    print("press 3 'Menstruation'")
    print("press 4 'Exit'")
    print("======================")

    try:
        ch1=int(input("\nPress the key : "))
    except ValueError :
        print("\n======================")
        print("***Invalid key***")   
        print("\npress a digit") 
        print("======================")
    else:
        if ch1==1:
            print("Basic Mode selected...")
            basic()
        elif ch1==2:
            print("scientific mode selected...")
            scientific()
        elif ch1==3:
            print("Mensuration mode selected...")
            mensuration()
        elif ch1 == 4:
            print("\nExiting...")
            print("\n\nThank you...")
            break
        else:
            print("\n Invalid key\npress a digit 1 - 4")
                   




