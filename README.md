Selenium Login Automation

This project automates login testing on the-internet.herokuapp.com/login using Selenium and Python.

Features

* Automates valid login test with username and password
* Uses ChromeDriver for browser automation
* Generates simple text reports after test run
* Structured with separate test files and reporting

Requirements

* Python 3.x
* Selenium library (pip install selenium)
* Chrome browser
* ChromeDriver matching your Chrome version (place chromedriver.exe in project root)

How to Run

1. Clone this repository
2. Ensure chromedriver.exe is in the project folder
3. Open terminal and run:

python run\_tests.py

4. Check the reports folder for test results

Folder Structure

selenium\_project/
├── chromedriver.exe
├── run\_tests.py
├── reports/
└── tests/
└── test\_login.py
