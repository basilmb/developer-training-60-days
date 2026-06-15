def add(num1, num2):
   return num1 + num2
def subtract(num1, num2):
   return num1 - num2
def multiply(num1, num2):
   return num1 * num2
def divide(num1, num2):
   if num2 == 0:
       return "Error: Cannot divide by zero"
   else:
       return num1 / num2
   
def calculator():
    try:
        current_result = float(input("enter first number: "))
    except ValueError:
        print("invalid number")
        
    while True:
        operation = input("choose an operation: \n + : add \n - : subtract \n * : multiply \n / : divide \n")
        if operation not in ["+", "-", "*", "/"]:
            print("invalid selection")
            continue
        
        try:
            second_number = float(input("enter second number: "))
        except ValueError:
            print("invalid number")
            continue

        match operation:
            case "+" : 
                current_result = add(current_result, second_number)
            case "-" :
                current_result = subtract(current_result, second_number)
            case "*" :
                current_result = multiply(current_result, second_number)
            case "/" :
                result = divide(current_result, second_number)
                if isinstance(result, str):
                    print(result)
                    continue
                current_result = result
            case _:
                print("Invalid operation selected")
                
        print(f"Result: {current_result}")
                
        choice = input("\n continue? (y/n): ")
        if choice != "y":
            print(f"final result: {current_result}")
            print("exiting calculator")
            break
        
if __name__ == "__main__":
    calculator()
        
            
            