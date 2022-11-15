
# Your Household Monthly Budget
A simple app allowing single user to populate a google spreadsheet with income and spending to keep track of Monthly Household Budget.

The household Monthly Budget app will provide user with:

1. Easy way to quickly update income and spendings
2. Calculate the spendings and funds left available after each update
3. Populate a google spreadsheet with the information and calculations for further use
4. Provide user with a short summary after data entry is succesfully done
5. Allow user to input negative quantities in Daily spendings for any refunds received from returned purchases

![mockup](https://github.comADD mockup pic)

Visit the Deployed website [here](https://skyforgeruk.github.io/Project_2_RPSSL/)
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


## Flow chart

!!!! ADD INFO of Data chart of the flow of the app !!!

## Existing Features

- User I queried if they want to update the set monthly income and spendings:
    - Needs to be done only once a month
    - If information needs to be amended then user has an option to do so
    - Option to not to have to update set info every thime app is launched saves time

 ![Input choice screenshot](https://github.com/SkyForgerUK/Project_2_RPSSL/blob/main/docs/screenshot-main.jpg)

<br>
<details>
  <summary>Pop-up page screenshot</summary>

 ![Pop-up page screenshot](https://github.com/SkyForgerUK/Project_2_RPSSL/blob/main/docs/pop-up-screen.jpg)
</details>
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

- After fixes one line still remains:
    - C0114: Missing module docstring (missing-module-docstring) - in order to fix pylint C0114 function needs disabling

- Code rated at 9.94/10 after fixes.

### Test cases 
<br>

- __User Cases__

!!!!! ADD INFO HERE !!!!
  
### Fixed bugs
- __Values would not show 2 decimal places__
    - fixed using f string formating method

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



