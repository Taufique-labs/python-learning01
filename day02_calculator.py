num1 = int(input("Enter your num1:"))
num2 = int(input("Enter your num2:"))

operator = input("Enter your operator (+,-,*,/):")

match operator:
    
    case '+':
        print("Sum:",num1+num2)
    case '-':
        print("Difference:",num1-num2)
    case '*':
        print("Product:",num1*num2)
    case '/':
        if num2 == 0:
            print("Undefined.")
        else:
            print("Division:",num1/num2)
    case _:
        print("Invalid operator.")