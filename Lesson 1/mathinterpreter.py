# Prompt the user for an arithmetic expression
expression = input("Expression: ")

# Calculate and output the result as a floating-point value formatted to one decimal place
x, y, z = expression.split(" ") # Split the values and stores them on these variables

match y: # Check what operator is Y and do the right operation
    case "+":
        print(float(int(x) + int(z)))
    case "-":
        print(float(int(x) - int(z)))
    case "*":
        print(float(int(x) * int(z)))
    case "/":
        print(float(int(x) / int(z)))