######## DEFINE FUNCTIONS ############################
from textwrap import dedent # bothered me to have the output out of format

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False
# rather than running all as a single loop, as suggested in the assignment,
# I made them into a few functions. the thought being, , 
# if this were a wider program, the process could be more easily reapeated.

def repeat_calc (answer=''): #allows repeat without more nesting (more readable?)
    if answer.upper() == 'Y':
        return calculator_function()
    elif answer.upper() == 'N':
        prompt("Thank you, have a wonderful day!")
    elif answer == '':
        prompt(dedent("""
            Please enter "y" (yes) to calculate again or "n" 
            (no) to exit the program
        """))
        answer = input()
        return repeat_calc(answer)
    else:
        prompt("Please limit response to either 'y' or 'n'")
        return repeat_calc()
    
def calculator_function():
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt(dedent("""
            Hmm... that doesn't look like a valid number. 
            Please try again. What is the first number?
        """))
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt(dedent("""
            Hmm... that doesn't look like a valid number. 
            Please try again. 
            What is the second number?
        """))
        number2 = input()

    prompt(dedent("""
        What operation would you like to perform?
        1) Add 2) Subtract 3) Multiply 4) Divide
    """))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4")
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(f"The result is {output}")

    prompt('Would you like to make another calculation? Y/n')
    answer = input()
    repeat_calc(answer)

############################## START PROGRAM #################################

prompt('Welcome to Calculator!')

calculator_function()




