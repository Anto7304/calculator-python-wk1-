print("Please enter two numbers and operation you want to perform")

num1 = int(input("enter a number : "))
operator = input("Enter an operator -,+,%,*,/,**,// : ")
num2 = int(input("enter another number : "))


if operator == '+':
    results = num1 + num2
    print(f"{num1} {operator} {num2} = {results}")

elif operator == '-':
    results = num1 - num2
    print(f"{num1} {operator} {num2} = {results}")
elif operator == '*':
    results = num1 * num2
    print(f"{num1} {operator} {num2} = {results}")
elif operator == '/':
    results = num1 / num2
    print(f"{num1} {operator} {num2} = {results}")
elif operator == '%':
    results = num1 % num2
    print(f"{num1} {operator} {num2} = {results}")

elif operator == '//':
    results = num1 // num2
    print(f"{num1} {operator} {num2} = {results}")

elif operator == '**':
    results = num1 ** num2
    print(f"{num1} {operator} {num2} = {results}")

else:
    print("Undefined")
    


