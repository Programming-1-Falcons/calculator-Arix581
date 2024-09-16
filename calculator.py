"""
This is a calculator program that should probably be able to perform the following functions:

Add
Subtract
Multiply
Divide
Exponentiate
Modulus (Give remainder?)
Floor Divide
"""

operations = """add
subtract
multiply
divide
floor divide
remainder divide (modulus)
exponentiation
What would you like to do?
Enter the first letter of the operation. """.title()
active = True
print("Welcome to the calculator")
while active:
# Get the mode of the program, as well as the numbers to be operated on
    print()
    while True:
        print("Available operations:".center(27,"-"))
        mode = input(operations).lower()
        if mode.startswith("a") | mode.startswith("s") | mode.startswith("m") | mode.startswith("d") | mode.startswith("e") | mode.startswith("f") | mode.startswith("r"):
            break
        else:
            print()
            print("That's not a mode, silly.")
            print()
    number1 = float(input("What's the first number? "))
    number2 = float(input("What's the second number? "))
    digits = int(input("How many digits would you like to round to? "))

    output = 0
    # Perform the operation and update the mode to a smarter sounding word for output
    if (mode.startswith("a")): # Addition
        output = number1 + number2
        mode = "addition"
    elif (mode.startswith("s")): # Subtraction
        output = number1 - number2
        mode = "subtraction"
    elif (mode.startswith("m")):
        output = round(number1 * number2, digits)
        mode = "multiplication"
    elif (mode.startswith("d")):
        output = round(number1 / number2, digits)
        mode = "division"
    elif (mode.startswith("e")):
        output = round(number1 ** number2, digits)
        mode = "exponentation"
    elif (mode.startswith("f")):
        output = number1 // number2
        mode = "floored division"
    elif (mode.startswith("r")):
        # Add Main division as well (Eg 5%2 = 2 R 1 as output)
        output = str(int(number1 // number2)) + " R "
        temp = number1 % number2
        if temp == int(temp):
            output += str(int(temp))
        else:
            output += str(temp)
        mode = "modulus"
    
    # Output the result
    print("The end result of the", mode, "operation between", number1, "and", number2, "is", round(output, digits))
    print()
    if input("Do you want to continue? y/n: ").lower().startswith("n"):
        active = False
print("Good bye!")
print("""I also did the rounding ability
I also have other mathematical processes
I also think that having the fancy input shower thingy where you enter a single letter and it works
I was able to get input validation on the operation input but not on the numbers""")