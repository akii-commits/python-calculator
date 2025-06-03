import math

# reccusrsion should be updated 
# make a function for reccursion for a specific code
# output ui structure update

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
        mode() #mode() is not defined merge this to main menu 
    elif choice=="yes":
        print("basic mode continues..")
        basic()
    else:
        print("***Invalid key***")
        msg()


            
msg()        

            
 



        






