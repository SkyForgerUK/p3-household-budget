
# Your Household Monthly Budget
A simple program allowing single user to populate a google spreadsheet with income and spending to keep track of Monthly Household Budget.

The household Monthly Budget program will provide user with:

1. Easy way to quickly update income and spendings
2. Calculate the spendings and funds left available after each update
3. Populate a google spreadsheet with the information and calculations for further use
4. Provide user with a short summary after data entry is succesfully done

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
    - To have usable google spreadsheet after using the program.


## Existing Features
There is one Home page including:

- Landing page
- Pop-up window explaining the rules of the game

### Navigation Bar and Footer
Both Nav bar and footer are responsive to the size of the screen being used to read the website.
- __Navigation Bar:__
    - Nav bar holds abbreviation of the game's full name and a stylised button that brings up rules contained in a pop-up window.
- __Footer:__
    - Footer contains full name of the game and is used to give the site a better overall look.
### Landing Page
- __Game Area:__
    - Holds the:
        - Score area - where the current score is kept
        - Chosen card area - where the user's and computers chosen cards are shown
        - Interactive text area - instructs user and provides feedback on choice made - win, lose or draw
        - Card area - holding 3 cards for the user to chose and play from 

<details>
  <summary>Landing Page screenshot</summary>

 ![Landing Page screenshot](https://github.com/SkyForgerUK/Project_2_RPSSL/blob/main/docs/screenshot-main.jpg)
</details>
<br>
<details>
  <summary>Pop-up page screenshot</summary>

 ![Pop-up page screenshot](https://github.com/SkyForgerUK/Project_2_RPSSL/blob/main/docs/pop-up-screen.jpg)
</details>
<br>

## Features left to implement
- __Multiuser access__
    - Current goal was to have the program serve one user per household, but using UUID a multi user exoperience could be provided.



## Data Model

!!!! ADD INFO !!!

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

- Aftter fixes one line still remains:
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

  <br>  

### Supported Screens, Browsers and Performance
### Browsers
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
### Screens
- Huawei P20 Pro
- Huawei P30 Mate
- iPhone 13 Pro
- iPhone 11


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
    - Program will run in the TERMINAL

<details>

  <summary>Link Page screenshot</summary>

   ![Published via GitPod](https://github.com/SkyForgerUKADD GITPOD DEPLOY PIC)
  
</details> 
<br>   

## Credits
### Content
- All content created by the project developer, except of:
  - Error check base code which was taken from Love Sandwitches project and mmodified to fit the developers needs
### Media
- stackowerflow was used to problemsolve various code issues



