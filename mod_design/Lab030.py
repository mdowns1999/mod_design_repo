# 1. Name:
#      Mike Downs
# 2. Assignment Name:
#      Lab 03: Calendar
# 3. Assignment Description:
#      This program is supposed to creat a calendar based on what month and year the user wants.  The program will then figure out if it is a leap year, what day the first of the month starts on, and display it to the user.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the calender to start on the right day.  I had all my functions working except my total_days.  After some help from a classmate, I found out instead of 
#starting th etotal amount of days from 0, it has to be 365 days.  THen suddenly everything made senese and everything lined up correctly.
# 5. How long did it take for you to complete the assignment?
#      3 Hours


def main():
    """This Main function will call the rest of the other functions of the calendar.  
    This function will also handle the user input and any user input errors """

    #This while loop sees if the month inputed by the user is a valid month.
    valid_month = False
    while not valid_month:
        user_month = input('Enter a month number: ')
        if user_month.isnumeric():
            user_month = int(user_month)
            if 0 < user_month < 13:
                valid_month = True
            else:
                print(f'Month must be between 1 and 12. You entered {user_month}.')
                valid_month = False
        else:
            print(f'Please enter an integer You entered {user_month}.')
            valid_month = False


    #This while loop determines if the year entered by the user is valid.  It will check if it is an integer and if it is greater than or equal to 1753.
    valid_year = False
    while not valid_year:
            user_year = input('Enter year: ')
            if user_year.isnumeric():
                user_year = int(user_year)
                if user_year >= 1753:
                    valid_year = True
                else:
                    print(f'Year must be 1753 or later. You entered {user_year}.')
                    valid_year = False
            else:
                print(f'Please enter an integer You entered {user_year}.')
                valid_year = False

    total = total_days(user_year, user_month)
    
    dom = num_days_month(user_month, user_year)


    first_day = first_day_month(total)


    print()
    display_table(first_day, dom)
    print()

def first_day_month(total_days):
    """This Function will take an amount of days and return a number that says what day of the week the month will start on."""
    return total_days % 7

def total_days(user_year, user_month):
    """This Function will calculate th etotal amount of days between the start year and the year the user entered.  It will also take into acount how many months have passed in the users year"""
    total = 365
    start_year = 1753

    #This loop calculates the user_year minus 1753.  It will go through each year and add up the total amount of days each year.
    for year in range(start_year, user_year):
        if is_leap_year(year):
            total += 366
        else:
            total += 365

    for i in range(1, user_month):
        total += num_days_month(i , user_year)


    return total

def num_days_month(user_month, user_year):
    """This function will determine the amount of days the user needs based on a desired month.
    Each number is based on what number it is.  FOr example, January is 1 or November is 11."""
    month_list_1 = [1,3,5,7,8,10,12] # Months of Jan, Mar, May, July, Aug, Oct, and Dec
    month_list_2 = [4,6,9,11] # Months of Apr, Jun, Sept, and Nov

    if user_month in month_list_1:
        return 31
    elif user_month in month_list_2:
        return 30
    elif user_month == 2: # This else if accounts for Feb sometimes having 28 days or 29 days.
        if is_leap_year(user_year):
            return 29
        else:
            return 28

def is_leap_year(year):
    """This function will determine if a given year is a leap year or not."""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline


main()