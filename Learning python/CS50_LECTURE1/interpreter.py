#asking user to enter an arithimatic expression
expression = input("Please enter an arithimatic expression: ")
#splitting the expression into a list of strings, then converting the first and last elements into integers and storing the operator in a variable.
expression = expression.split(" ")
x = float(expression[0]) #the first number in the expression
y = float(expression[2]) #the second number in the expression
z = expression[1] #the operator in the expression

if z == "+":
    print(float(round(x + y, 1)))
elif z == "-":
    print(float(round(x - y, 1)))
elif z == "*":
    print(float(round(x * y, 1)))
elif z == "/":
    print(float(round(x / y, 1)))
elif z == "**":
    print(float(round(x ** y, 1)))
elif z == "%":
    print(float(round(x % y, 1)))  
else:
    print("Invalid operator")