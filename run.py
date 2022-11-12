from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('monthly_budget')

def get_choice_for_set():
    """
    Offer user to chose to update monthly set income and expenses.
    If user chooses "n" for not to enter, then break function. 
    If user chooses "y" then is moved to input point.
    """
    while True:
        print("\nWould you like to update set monthly income and expenses?")

        choice = input("Please choose y/n: ")

        if choice == "y":
            return True
        elif choice == "n":
            break
        else:
            print("\nPlease choose between y for yes or n for no")


def get_set_income_expense_data():
    """
    Get set monthly income and expense data from user.
    Run a while loop to collect a string of data from the user
    via the terminal, consisting of exactly 6 numbers, seperated by
    comma. Loop will keep requesting data until it is valid.
    """
    while True:
        print("\nPlease enter set monthly data")
        print("Data must be 6 numbers, seperated by commas")
        print("Example: 10,20,30,40,50,60\n")
        print("Categories are:")
        pprint(["1. Total Salary", "2. Other Income", "3. Monthly Morgage", "4. Loans", "5. Utility Bills", "6. Other Set Expenses"])

        set_data_str = input("\n Enter daily expenses here: ")

        set_in_out_data = set_data_str.split(",")
        validate_set_data(set_in_out_data)

        if validate_set_data(set_in_out_data):
            print("Entered information is valid!")
            break

    return set_in_out_data


def validate_set_data(values):
    """
    Inside the try, all string values converetd to floats.
    Raises ValueError if string cannot be converted in float
    or if there are not exactly 8 values entered
    """
    try:
        [float(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"6 values are requires, you entered {len(values)}"
            )
    except ValueError as error:
        print(f"\nInvalid data: {error}, please try again.\n")
        return False

    return True


def update_set_in_and_out_worksheet(set_data):
    """
    Update set_in_and_out worksheet by replacing
    already existing data in row 2
    """
    print("Updating Set Income and expenses worksheet...\n")
    set_in_and_out_worksheet = SHEET.worksheet("set_in_and_out")
    set_in_and_out_worksheet.delete_rows(2)
    set_in_and_out_worksheet.append_row(set_data)
    print("Daily Expenses worksheet uopdated successfully.\n")


def set_in_out():
    """
    Combine users choice to update the set income or not with
    enter the set data if users choice was yes.
    """
    if get_choice_for_set():
        set_data = get_set_income_expense_data()
        update_set_in_and_out_worksheet(set_data)


def get_daily_expenses_data():
    """
    Get daily expenses figures input from the user
    Run a while loop to collect a string of data from the user
    via the terminal, string must be a collection of 8 numbers
    seperated by comma. The loop will keep requesting data,
    until it is valid.
    """
    while True:
        print("\n\nPlease enter today's expenses.\n")
        print("Data must be 8 numbers, seperated by commas")
        print("Example: 10,20,30,40,50,60,70,80\n")
        print("Categories are:")
        pprint(["1. Food", "2. Hygiene and Cleaning", "3. Clothing and Shoes", "4. Pet Supplies", "5. Car and Fuel", "6. Gifts", "7. Large Purchases", "8. Other Expenses"])
        

        
        data_str = input("\n Enter daily expenses here: ")

        

        daily_expenses_data_check = data_str.split(",")
        validate_data(daily_expenses_data_check)

        data_str_total = the_date + ',' + data_str
        daily_expenses_data = data_str_total.split(",")

        if validate_data(daily_expenses_data_check):
            print("Entered information is valid!")
            break
        
                 
    return daily_expenses_data


def validate_data(values):
    """
    Inside the try, all string values converetd to floats.
    Raises ValueError if string cannot be converted in float
    or if there are not exactly 8 values entered
    """
    try:
        [float(value) for value in values]
        if len(values) != 8:
            raise ValueError(
                f"8 values are requires, you entered {len(values)}"
            )
    except ValueError as error:
        print(f"invalid data: {error}, please try again.\n")
        return False

    return True


def update_daily_expenses_worksheet(data):
    """
    Update daily_expenses worksheet and a new row with the
    list data provided
    """
    print("Updating Daily Expenses worksheet...\n")
    daily_expenses_worksheet = SHEET.worksheet("daily_expenses")
    daily_expenses_worksheet.append_row(data)
    print("Daily Expenses worksheet uopdated successfully.\n")

now = datetime.now()
the_date = now.strftime("%d/%m/%Y")
set_in_out()
data = get_daily_expenses_data()
update_daily_expenses_worksheet(data)


print(data)
print(type(data))
print(the_date)
print(type(the_date))
