import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('monthly_budget')


def get_daily_expenses_data():
    """
    Get daily expenses figures input fromthe user
    Run a while loop to collect a string of data from the user
    via the terminal, string must be a collection of 8 numbers
    seperated by comma. The loop will keep requesting data,
    until it is valid
    """
    while True:
        print("Please enter today's expenses.\n")
        print("Data must be 8 numbers, seperated by commas")
        print("Example: 10,20,30,40,50,60,70,80\n")
        print("Categories are:")
        pprint(["1. Food", "2. Hygiene and Cleaning", "3. Clothing and Shoes", "4. Pet Supplies", "5. Car and Fuel", "6. Gifts", "7. Large Purchases", "8. Other Expenses"])
     
        data_str = input("\n Enter daily expenses here: ")

        daily_expenses_data = data_str.split(",")
        validate_data(daily_expenses_data)

        if validate_data(daily_expenses_data):
            print("Entered information is valid!")
            break

    return daily_expenses_data


def validate_data(values):
    """
    Inside the try, all string values converetd to floats.
    Rases ValueError if string cannot be converted in float
    or if there are not exactly 8 values entered
    """
    try:
        [float(value) for value in values]
        if len(values) != 8:
            raise ValueError(
                f"8 values are requires, you entered {len(values)}"
            )
    except ValueError as er:
        print(f"invalid data: {er}, please try again.\n")
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


data = get_daily_expenses_data()
update_daily_expenses_worksheet(data)

