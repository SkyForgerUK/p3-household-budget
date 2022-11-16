
# Your Household Monthly Budget
A simple app allowing single user to populate a google spreadsheet with income and spending to keep track of Monthly Household Budget.

The Monthly Household Budget app will provide user with:

1. Easy way to quickly update income and spendings
2. Calculate the spendings and funds left available after each update
3. Populate a google spreadsheet with the information and calculations for further use
4. Provide user with a short summary after data entry is succesfully done
5. Allow user to input negative quantities in spendings for any refunds received from returned purchases

![mockup](https://github.comADD mockup pic)

Visit the Deployed app [here](https://p3-monthly-budget.herokuapp.com/)

Visit the Google Spreadsheet [here](https://docs.google.com/spreadsheets/d/1tGRlS6nOt_KR-9JTXAoTrjGjLxxa7G9GL4ZY24hSXQU/edit#gid=0)

## Table of Content
- [User Stories](#user-stories)
- [Existing Features](#existing-features)
- [Technology](#technology)
- [Testing](#testing)
  - [Code Validation - pylint run.py](#code-validation---pylint run.py)
  - [Test Cases](#test-cases)
  - [General Testing](#general-testing)
  - [Fixed Bugs](#fixed-bugs)
  - [Not Fixed Bugs](#not-fixed-bugs)
  - [Supported Screens, Browsers and Performance](#supported-screens-browsers-and-performance)
- [Deployment](#deployment)
- [Credits](#credits)
<br>


## User Stories 

- As a user I want:
    - To understand what data needs to be entered.
    - See feedback if entered data is incorrect and hints on what was incorrect.
    - To see update and calcullation being in progress.
    - To receive a summary of the current income and spending state.
    - To have usable google spreadsheet after using the app.


## Flowchart

![Flowchart screenshot](https://git)

## Existing Features

- User is queried if they want to update the set monthly income and spendings:
    - Needs to be done only once a month
    - If information needs to be amended then user has an option to do so
    - Option to not to have to update set info every thime app is launched saves time

![Update Set Values screenshot](https://github.com/SkyForgerUK/Project_2_RPSSL/blob/main/docs/screenshot-main.jpg)

<br>

- User is informed what the categories to update are and the format the data needs to be on both - Set Income and spendings and Daily spendings.

![Information screenshot](https://github.com/SkyForgerUK/Project_2_RPSSL/blob/main/docs/pop-up-screen.jpg)

<br>

- User is informed if invalid data is entered and promted to enter the data again.

![Invalid number count screenshot](https://github.com/SkyForgerUK/Project_2_RPSSL/blob/main/docs/pop-up-screen.jpg)
![Invalid data format screenshot](https://github.com/SkyForgerUK/Project_2_RPSSL/blob/main/docs/pop-up-screen.jpg)

<br>

- User is visualy informed that the app is doing calculations and updates.

![Updating screenshot](https://github.com/SkyForgerUK/Project_2_RPSSL/blob/main/docs/pop-up-screen.jpg)

<br>

- User is provided with a summary of Income, Expenses and Money left over to spend.

![Summary screenshot](https://github.com/SkyForgerUK/Project_2_RPSSL/blob/main/docs/pop-up-screen.jpg)

<br>

## Features left to implement
- __Multiuser access__
    - Current goal was to have the app serve one user per household, but using UUID a multi user exoperience could be provided.
- __Create a a solution for refunds__
    - Create an additional input for user to submit daily refunds, so the current method of negative quantity input can be disabled.

### Languages

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Software and Framework Libraries

- [Mock-up generator](https://websitemockupgenerator.com/)
    - To generate a mock-up image for the Readme file
- [Heroku](https://heroku.com/)
    - To publish the finished project
- [GitPod](https://www.gitpod.io/)
    - To use as a platform for coding

## Testing
Testing was carried out by project developer using pylint run.py in Gitpod environment. 
### Code Validation - pylint run.py
- On first time testing 17 error lines were given:
    - 3 lines of text too long
    - 1 line of unneccessary elif function
    - 9 lines of c0209: formatting a regular string which could be a f-string (consider-using-f-string) error
    - 1 line of C0114: Missing module docstring (missing-module-docstring)

- On second run 1 error was shown:
    - C0114: Missing module docstring (missing-module-docstring) - in order to fix pylint C0114 function needs disabling

- On third run - all errors have been cleared
    - Code rated at 10/10 after fixes.


### Testing  
    |Action | Expected behaviour | Result|
    |-------|--------------------|-------|
    |Run Program | Greeting message and a propt to choose to update Set Income and Expenses apears | Pass |
    |When prompted to enter y or n, type any other character | Error message apears explaining issue and user is prompted to enter the y or n again | Pass |
    |Choose not to update the Set values | updating is bypassed and usser is taken to update Daily expenses | Pass |
    |Choose to update the Set values| User is provided with a list of categoriess and an example of acceptable data format | Pass |
    |Input incorrect data in Daily expenses update | Error message apears explaining issue and user is prompted to enter the data again | Pass |
    |Correct data is logged  | Processing and updating lines for varous categories are shown and at the end a summary of expenses, income and money left is shown in the portal | Pass |
<br>  

### Fixed bugs
- __Values would not show 2 decimal places__
    - Fixed using f string formating method

 ### Not fixed bugs
 - __No bugs found__

<br >

## Deployment
- __Via Heroku__
    - Open a web browser
    - Go to address https://heroku.com/
    - Log in my Heroku account
    - Click on "Create new app"
    - Use unique app name
    - Choose reagon (Europe if based in Europe)
    - In Settings tab under Config Vars add creds.json info and PORT 8000 
    - Click "Add Buildpack" and add "python" and "nodejs"
    - Head to Deploy section and choose Github as deployment method
    - On Pop-up window enter Github password
    - Find repository for project using search bar and repository name and click "connect"
    - Scroll down and choose "Enable Automatic Deploys" and after that  - once "Deploy Branch"
    - Once deployment is successfull click on "View" to access the deployed page
<details>

  <summary>Link Page screenshot</summary>

   ![Published via Heroku](https://github.com/SkyForgerUK/ADD DEPLOYED PIC)
  
</details> 
<br>   

- __Via GitPod__
    - Open a web browser
    - Go to address https://github.com/SkyForgerUK/p3-household-budget
    - Click on "Gitpod" button to launch the application
    - In TERMINAL section type in command "python3 run.py"
    - App will run in the TERMINAL

<details>

  <summary>Link Page screenshot</summary>

   ![Published via GitPod](https://github.com/SkyForgerUKADD GITPOD DEPLOY PIC)
  
</details> 
<br>   

## Credits
### Content
- All content created by the project developer, except of:g
  - Error check base code which was taken from Love Sandwitches project and mmodified to fit the developers needs
### Media
- stackowerflow was used to problemsolve various code issues



