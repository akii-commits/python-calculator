import math
def trig2():
    print()
    tr=input("enter trignometric ratio:")
    if tr in ['sin','cos','tan','sec','cosec','cot']:
        print("Enter angle")
        ang=int(input(tr))
        print()
        rd2=math.radians(ang)
        if tr=="sin":
            print("sin",ang,"=",math.sin(rd2))
        elif tr=="cos":
            print("cos",ang,"=",math.cos(rd2))
        elif tr=="tan":
            print("tan",ang,"=",math.tan(rd2))
        elif tr=="sec":
            print("sec",ang,"=",math.sec(rd2))
        elif tr=="cot":
            print("cot",ang,"=",math.cot(rd2))
        elif tr=="cosec":
            print("cosec",ang,"=",math.cosec(rd2))
        return rd2
    else:
        print("Invalid Input")
        trig2()

def tmathx(m=[]):
    a=trig()
    b=sec()
    c=trig2()
    d=op(a,c,b)
    print('ans =',d)
    data(d,l1)
    t_outro()

def t_outro():   
    if exit()==True:
        b=sec()
        c=trig2()
        print('ans =',op(l1[0],c,b))
        t_outro()


def data(d,m=[]):
    m.append(d)

def mathx(m=[]):
    a=lg()
    b=sec()
    c=lg_2()
    d=op(a,c,b)
    print('ans =',op(a,c,b))
    data(d,l)
    outro()

def outro():    
    if exit()==True:
        b=sec()
        c=lg_2()
        print('ans =',op(l[0],c,b))
        outro()

    else:
        mathx()

def lg_2():
    print("enter the log value")
    print()
    try:
        l=int(input("log"))
        d2=math.log(l)
        print("log",l,"=",math.log(l))
        return d2
    except ValueError:
        print("Invalid Value")
        print("Try again")
        lg_2()

def op(a=float,b=float,m=""):
    if m=="+":
        return a+b
    elif m=="-":
        return a-b
    elif m=="*":
        return a*b
    elif m=="/":
        return a/b

def sec():
    c1=input("Perform Aritematical operations? 'y'/'n':")
    if c1=='y':
        c2=input("select operator '+-*/':")
        if c2 in '+-*/':
            return c2
        
        else:
            print("INAVAD INPUT")
            print()
            print(c2,"is not an arithematical operator")
            print()
            input("press ENTER to continue")
            return sec()
    elif c1=='n':
        exit()
    else:
        print("INVALID INPUT")
        print()
        return sec()
        
def exit():
    cont_=input("Would you like to continue 'y'/'n':")
    if cont_=="y":
        return True
    elif cont_=="n":
        print()
        ex=input("Return to scientific mode ..'y'/'n':")
        if ex=='y' or ex=='Y':
            scmd()


        
        

def lg():
    print("enter the log value")
    print()
    try:
        l=int(input("log"))
        d1=math.log(l)
        print("log",l,"=",math.log(l))
        return d1
    except ValueError:
        print("Invalid Value")
        print("Try again")
        lg()

        

        
        
    



    





    






def trig():
    print()
    tr=input("enter trignometric ratio:")
    if tr in ['sin','cos','tan','sec','cosec','cot']:
        print("Enter angle")
        ang=int(input(tr))
        print()
        rd=math.radians(ang)
        if tr=="sin":
            print("sin",ang,"=",math.sin(rd))
        elif tr=="cos":
            print("cos",ang,"=",math.cos(rd))
        elif tr=="tan":
            print("tan",ang,"=",math.tan(rd))
        elif tr=="sec":
            print("sec",ang,"=",math.sec(rd))
        elif tr=="cot":
            print("cot",ang,"=",math.cot(rd))
        elif tr=="cosec":
            print("cosec",ang,"=",math.cosec(rd))
        return rd
    else:
        print("Invalid Input")
        trig()


 
        


    
    





print("What oppretion would you like to choose?")
print()
print("=========OPERATIONS=========")
print("Trignometric ratios")
print("Logarithmic")
print("Factorial ")
print("Gif function ")
print("Exponential")
print()
cmd=input("Press ENTER to coninue:")

def scmd():
    print()
    print("press 'T' Trignometric ratios")
    print("press 'L' Logarithmic")
    print("press 'F' Factorial ")
    print("press 'G' Gif function ")
    print("press 'E' Exponential")
    print("press 'R' to Return to  Mode menu")
    print()

    chs=input("SELECT any operation:")
    print()
    if chs=='T' or chs=='t':
        print("====Trignometric Ratios====")
        l1=[]
        tmathx()
    elif chs=='L' or chs=="l":
        print("=====Logarithm values=====")
        l=[]
        mathx()
        

    elif chs=="F" or chs=="f":
        print("=====Factorials======")
    elif chs=="G" or chs=="g":
        print("======Gif Functions======")
    elif chs=="E" or chs=="e":
        print("=====Exponential=====")
    elif chs=="R" or chs=="r":
        print()
        print("Returning to Mode selector...")
        print()
        input("Press ENTER to continue")
        # mode()

    else:
        print("Invalid key")
        scmd()
l1=[]
l=[]
scmd()





