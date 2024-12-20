### Assumptions ##############################################################
# interest compounds monthly
# formula for calculating interest is 'm = p * (j / (1 - (1 + j) ** (-n)))'
    # m = mo. payments
    # p = loan amount
    # j = monthly interest rate
    # n = loan duration in months
### Goals ####################################################################
# using user input, determine (print) the monthly payments in "$123.45" format
# account for fringe cases

def prompt(message):                              # for cleaner user interface
    print(f'==> {message}')

from textwrap import dedent                # helps with some formatting issues
import re                                  # for handling non-numerical inputs

def is_blank(blank):
    while blank != True:
        if blank.strip():
            break
        else:
            blank = input('Oops, feild is blank, try again: ')

def is_num(inputs):
    inputs = re.sub(r'[\D]', '', inputs) #removes $,. etc... for type testing
    while type(inputs) == str:
        try:
            inputs = int(inputs)    
        except ValueError as e:
            inputs = input(dedent('''
                    ERR: Unexpected input type, 
                    please re-enter your data (numeric values only). 
                    '''))
            inputs = str(inputs)


print("""

********************* PyLoan_1.0 *********************************************

""")

prompt("""Thank you for choosing PyLoan for all you loan calculating needs. 
    In order to assist you, please enter the requested data when prompted. 

    Let\'s get started!
    """)
def mortgage_calculator ():
    global loan_amount
    prompt('First, what is the amount of your loan?')
    loan_amount = input('$ '.rjust(70, '-'))
    is_blank(loan_amount)                               #checks for falsy (blanks)
    is_num(loan_amount)                                 #checks for type
    loan_amount = re.sub(r'[^0-9.,]', '', loan_amount) #strips non-numbers [exc '.'','] for display purposes

    global loan_duration
    prompt('Second, what is the duration of your loan?')
    loan_duration = input('(in years) '.rjust(70, '-'))
    is_blank(loan_duration)
    is_num(loan_duration)
    loan_duration = re.sub(r'[^0-9.,]', '', loan_duration)

    global apr_year
    prompt('Last, what is the Annual Percentage Rate (APR) on this loan?')
    apr_year = input(' '.rjust(70, '-'))
    is_blank(apr_year)
    is_num(apr_year)
    apr_year = re.sub(r'[^0-9.,]', '', apr_year)

    global info_verify
    prompt(f'''Just to confirm: You have a {loan_duration}-year loan 
    for ${loan_amount} at {apr_year}%. Is that correct? (y/n)''')
    info_verify = input(' '.rjust(70, '-')).casefold()
   
    while info_verify:     #ensures ONLY y or n gets through            
        if info_verify == 'y':
            break
        elif info_verify == 'n':
            prompt("Please re-enter the correct values")
            return mortgage_calculator()
        elif info_verify == '':
            is_blank(info_verify)
        else: 
            prompt(dedent("""I'm sorry, I didn't understand your last 
    response.please answer 'y' for yes or 'n' for no."""))
        info_verify = input(' '.rjust(70, '-')).casefold()

    loan_amount = re.sub(r'[^0-9.]', '', loan_amount)      #normalizes inputs (if user put ',' '$' or '%') 
    loan_duration = re.sub(r'[^0-9.]', '', loan_duration)  #keeping '.' to not kill floats
    apr_year = re.sub(r'[^0-9.y]', '', apr_year)

    loan_amount = float(loan_amount)        
    loan_duration = float(loan_duration)
    apr_year = float(apr_year)

    month_dur = loan_duration * 12  

    if apr_year == 0:               #handles 0%interest
        global payment
        payment = loan_amount / month_dur
    else:
        global month_int            #handles non-zero interst
        month_int = (apr_year / 100) / 12
        payment = loan_amount * (month_int / 
        (1 - (1 + month_int) ** (- month_dur)))

    prompt(f'Your monthly payments for this loan will be ${payment:,.2f}')
    print()
    prompt('Would you like to make another calculation?')
    restart = input(' '.rjust(70, '-')).casefold()

    while restart:              #ensures ONLY y or n gets through
            if restart == 'y':
                print(' '.rjust(72, '*'))
                prompt("Ok, let's take it from the top.")
                mortgage_calculator()
            elif restart == 'n':
                prompt("Thank you, for choosing PyLoan. Goodbye.")
                break
            elif restart == '':
                is_blank(restart)
            else: 
                prompt(dedent("""I'm sorry, I didn't understand your last 
    response. please answer 'y' for yes or 'n' for no."""))
            restart = input(' '.rjust(70, '-')).casefold()    

mortgage_calculator() # stored as function for easy revisting
