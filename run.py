from datetime import datetime
from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('monthly_budget')

now = datetime.now()
the_date = now.strftime("%d/%m/%Y")
summary_sheet = SHEET.worksheet("summary")
set_sheet = SHEET.worksheet("set_in_and_out")


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
        print(f"\nInvalid data: {error}, please try again (numbers only).\n")
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
    total_income()
    set_total_expenses()


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
        print(f"invalid data: {error}, please try again (numbers only).\n")
        return False

    return True


def update_daily_expenses_worksheet(data):
    """
    Update daily_expenses worksheet and a new row with the
    list data provided
    """
    print("\nUpdating Daily Expenses worksheet...\n")
    daily_expenses_worksheet = SHEET.worksheet("daily_expenses")
    daily_expenses_worksheet.append_row(data)
    print("Daily Expenses worksheet updated successfully.\n")


def sum_daily_expenses():
    """
    Using a foor loop get all column values form daily_expenses sheet,
    sum them and hen return Values in a list format using a for loop.
    """
    daily = SHEET.worksheet("daily_expenses")

    sum_list = []
    for number in range(2, 10):
        only_numbers = daily.col_values(number)[1:]
        total_sum = sum(float(i) for i in only_numbers)
        formated_sum = "{:.2f}".format(total_sum)       
        sum_list.append(formated_sum)
    return sum_list


def update_total_expenses_sheet(daily_total_data):
    """
    Update daily_expenses worksheet by replacing
    already existing data in row 2
    """
    print("Updating Total Daily Expenses worksheet...\n")
    set_in_and_out_worksheet = SHEET.worksheet("total_daily_expenses")
    set_in_and_out_worksheet.delete_rows(2)
    set_in_and_out_worksheet.append_row(daily_total_data)
    print("Total Daily Expenses worksheet updated successfully.\n")


def total_income():
    """
    Retrieve Total Salary and Other Income values from set_in_and_out sheet
    and calculate the sum of them and update the Total Income cell in
    summary sheet.
    """
    salary = set_sheet.acell('A2').value
    other_income = set_sheet.acell('B2').value
    income_sum = float(salary) + float(other_income)
    form_income_sum = "{:.2f}".format(income_sum)
    print("Updating Total Income in Summary sheet...\n")
    summary_sheet.update_acell("A2", form_income_sum)
    print("Total Income updated successfully.\n")


def set_total_expenses():
    """
    Retrieve all Set Expenses values form set_in_and_out sheet
    and calculate the sum of them and update the Total Set Expenses
    cell in summary sheet.
    """
    set_expenses_mortgage = set_sheet.acell('C2').value
    set_expenses_loans = set_sheet.acell('D2').value
    set_expenses_utility = set_sheet.acell('E2').value
    set_expenses_other = set_sheet.acell('F2').value
    set_expenses_sum = float(set_expenses_mortgage) + float(set_expenses_loans) + float(set_expenses_utility) + float(set_expenses_other)
    form_set_expense_sum = "{:.2f}".format(set_expenses_sum)
    print("Updating Total Set Expenses in Summary sheet...\n")
    summary_sheet.update_acell("B2", form_set_expense_sum)
    print("Total Set Expenses updated successfully.\n")


def ccumulative_daily_expenses():
    """
    Retrieve total daily expenses from total_daily_expenses sheet, sum them and
    post them to Cumulative Daily Expenses in summary sheet.
    """
    total_d_expenses_sheet = SHEET.worksheet("total_daily_expenses")
    total_expense_list = total_d_expenses_sheet.row_values(2)
    total_exp = sum(float(i) for i in total_expense_list)
    sum_expenses = "{:.2f}".format(total_exp)
    print("Updating Cumulative Daily Expenses in Summary sheet...\n")
    summary_sheet.update_acell("C2", sum_expenses)
    print("Cumulative Daily Expenses updated successfully.\n")


def all_total_expenses():
    """
    Retrieve Total Set Expenses and Cumulative Daily Expenses from summary
    sheet and sum and update the sum value to Total Expenses in summary
    sheet.
    """
    total_set_expenses = summary_sheet.acell("B2").value
    cumulative_daily_expenses = summary_sheet.acell("C2").value
    total_expenses = "{:.2f}".format(float(total_set_expenses) + float(cumulative_daily_expenses))
    print("Updating Total Expenses in Summary sheet...\n")
    summary_sheet.update_acell("D2", total_expenses)
    print("Total Expenses updated successfully.\n")


def money_left():
    """
    Calculate money left by substracting total expense from total income from
    summary sheet and update the Money Left in summary sheet.
    """
    all_income = summary_sheet.acell("A2").value
    all_expenses = summary_sheet.acell("D2").value
    leftover = "{:.2f}".format(float(all_income) - float(all_expenses))
    print("Updating Money Left in Summary sheet...\n")
    summary_sheet.update_acell("E2", leftover)
    print("Money Left updated successfully.\n")


def main():
    """
    Holds all main functions to be run when program is activated.
    """
    set_in_out()
    data = get_daily_expenses_data()
    update_daily_expenses_worksheet(data)
    daily_total_data = sum_daily_expenses()
    update_total_expenses_sheet(daily_total_data)
    ccumulative_daily_expenses()
    all_total_expenses()
    money_left()


main()



#print(data)
#print(type(data))
#print(the_date)
#print(type(the_date))
