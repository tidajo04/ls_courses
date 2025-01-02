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

from textwrap import dedent                # helps with some formatting issues
import re                                  # for handling non-numerical inputs

def prompt(message):                              # for cleaner user interface
    print(f'==> {message}')

def is_blank(blank):
    while blank != True:
        if blank.strip():
            break
        else:
            blank = input('Oops, feild is blank, try again: ')
    return blank

def is_num(inputs):
    inputs = re.sub(r'[\D]', '', inputs) #removes $,. etc... for type testing
    while type(inputs) == str:
        try:
            inputs = float(inputs)    
        except ValueError as e:
            inputs = input(dedent('''
                    ERR: Unexpected input type, 
                    please re-enter your data (numeric values only). 
                    '''))
            inputs = str(inputs)

def get_started_msg():
    prompt("Let's get started!")

def get_loan_amount():
    prompt('First, what is the amount of your loan?')
    loan_amount = input('$ '.rjust(70, '-'))
    is_blank(loan_amount)                               #checks for falsy (blanks)
    is_num(loan_amount)                                 #checks for type
    loan_amount = re.sub(r'[^0-9.,]', '', loan_amount) #strips non-numbers [exc '.'','] for display purposes
    return loan_amount

def get_loan_dur():
    prompt('Second, what is the duration of your loan?')
    loan_duration = input('(in years) '.rjust(70, '-'))
    is_blank(loan_duration)
    is_num(loan_duration)
    loan_duration = re.sub(r'[^0-9.,]', '', loan_duration)
    return loan_duration
def get_apr():
    prompt('Last, what is the Annual Percentage Rate (APR) on this loan?')
    apr_year = input(' '.rjust(70, '-'))
    is_blank(apr_year)
    is_num(apr_year)
    apr_year = re.sub(r'[^0-9.,]', '', apr_year)
    return apr_year

def verify_info(duration, amount, apr):
    prompt(f'''Just to confirm: You have a {duration}-year loan 
    for ${amount} at {apr}%. Is that correct? (y/n)''')
    info_verify = input(' '.rjust(70, '-')).casefold()

    return info_verify

def calculate_monthly_payment(loan_amount, loan_duration, apr_year):

    loan_amount = re.sub(r'[^0-9.]', '', loan_amount)      #normalizes inputs (if user put ',' '$' or '%') 
    loan_duration = re.sub(r'[^0-9.]', '', loan_duration)  #keeping '.' to not kill floats
    apr_year = re.sub(r'[^0-9.y]', '', apr_year)

    loan_amount = float(loan_amount)        
    loan_duration = float(loan_duration)
    apr_year = float(apr_year)

    month_dur = loan_duration * 12  

    if apr_year == 0:               #handles 0%interest
        payment = loan_amount / month_dur  
    else:
        month_int = (apr_year / 100) / 12 #handles non-zero interst
        payment = loan_amount * (month_int / 
        (1 - (1 + month_int) ** (- month_dur)))
          
    return payment
    
def calculate_again_prompt():
    prompt('Would you like to make another calculation?')
    
    while True:
        restart = input(' '.rjust(70, '-')).casefold()
        if restart == 'y':
            print(' '.rjust(72, '*'))
            prompt("Ok, let's take it from the top.")
            return True
        elif restart == 'n':
            prompt("Thank you, for choosing PyLoan. Goodbye.")
            return False    
        else: 
            prompt("""I'm sorry, I didn't understand your last 
    response. please answer 'y' for yes or 'n' for no.""")
    

def mortgage_calculator ():
    
    loan_amount = get_loan_amount()
    loan_duration = get_loan_dur()
    apr_year = get_apr()

    info_verify = verify_info(loan_amount, loan_duration, apr_year)

    if info_verify != 'y':
        prompt(f'''Your response: \"{info_verify}\" does not confirm the correct
    values. Please re-enter the correct values and confirm with 'y'
    ''')
        return mortgage_calculator()
   
    payment = calculate_monthly_payment(loan_amount, loan_duration, apr_year)
    prompt((f'Your monthly payments for this loan will be ${payment:,.2f}') )
    
    print()
    
    restart = calculate_again_prompt()
    if restart:
        mortgage_calculator()
    else:
        return
      
############### START PROGRAM ################################################
print("""

********************* PyLoan_1.0 *********************************************

""")

prompt("""Thank you for choosing PyLoan for all you loan calculating needs. 
    In order to assist you, please enter the requested data when prompted. 
    """)
get_started_msg()

mortgage_calculator() # stored as function for easy revisting
