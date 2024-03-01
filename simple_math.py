num1 = float(input("Enter 1st number: "))
operator = input("Choose the operator (+ - * /): ") #operator variable can accept any value
num2 = float(input("Enter 2st number: "))

if operator == "+":
    total = num1 + num2
    print(f"Result= {total}")

else:
    print(f"{operator} is not a valid operator...")