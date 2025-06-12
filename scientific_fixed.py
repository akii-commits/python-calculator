import math

def msg():
    msg=input("\ndo you want to continue (y/n) :").lower()
    return msg == "y"

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
