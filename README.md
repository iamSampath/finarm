# FinArm

Inspired from the idea of Financial Freedom and value of time.
FinArm is a webApplication that supports users to tackle their debts
by providing IAS (Insights,analysis and simulations) on the users Debt situation.

[DEMO URL](https://youtu.be/lRqAJJK1LmY)


**Insights:**
What is the user current Debt Ratio.
This basically helps user to understand the debt ratio of all credit cards added by the user, In general keeping credit usage under 30% would be ideal for better offers.
What is Debt ratio for a current Loan/Card.
Debt-credit ratio for oen particular card.

**Analysis:**
What Benifits do the user have on a particular card.
What are the benefits of the card
What is the best card that can be used based on a situation.
Helps to udnerstand which card can be used for a specalized situation

**Simulations:**
How much time does it takes to Pay off a loan or card.
Simulation are key inorder to understand how much time it is going to take with only minimum payments.
How much interest will i pay on a particular card with varying factors.

**Folder Strucuture:**
The folder structure sticks to the traditional project structure
All the static resources like css,images and other media will be in the static folder
however for now i only used css.

static contains all the CSS files
Templates contains all html files which are used in the project
Tables.txt contains the table structure used
The db created for this application is called "finarm.db"


Templates: 
Templates contains 9 Html pages designed to serve the purpose of the application.
 index.html - Contains the description of the application and what it will be used for.
 login.html - This is the login page that will authenticate the users with their resources.
 layout.html - Layout contains most of the code for the header footer which is common across all the tempaltes, everyother templates will
               extend the layout.html.
 errorpage.html - Displayed when errors are popped up
 finadd.html -  contains form for adding financial information.
 homepage.html - This page is the home page when users logs in , and contains buttons for taking users to analysis and Adding financial information.
 aboutus.html - this page mostly contians informaiton about the developer, i am intending to get a facelift for this one :)
 analysis.html - This Page contains the I A S caliculated by the app for the user.
 registration.html - This page is needed registering the new user.
  
**Technologies used:**
* Python
* Bootstrap
* css
* Html5
* Flask.

**Application Type:**
Web Application


**Design choices:**
In the current implementaiton i moved away from standard CS50 libraries,
so that i can explore more about the Flask, Python. this choice made me to see how the
various things worked and gave much more confidence.

**Tables info:**
There are two tables used in this project
users - contains all the user information and contains all logins information.
fininfo - All the financial informaiton provided by the user will be stored inthis table.

**cdn:**
For the bootstrap js css libraries cdn has been used.

**Future Implementations that i am thinking:**
Although this project is build in for cs50, i am planning on using it furthermore with additional implementations
Moving all tables to GCP/AWS.
implementing a data loading from excel sheet
updating feature for all credit cards or loans
providing various debt payoff strategies.
Duedates for various cards/loans.
