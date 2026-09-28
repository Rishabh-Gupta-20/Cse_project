VITyarthi CSE Project
Apex Bank Support – Customer Care Helpline
 Project Description

Apex Bank Support is a simple Python-based Customer Care Helpline / IVR (Interactive Voice Response) System.

The project simulates what happens when a customer calls a bank's helpline number. The system displays different options and allows the user to select services such as checking account balance, blocking a lost or stolen debit card, getting loan and internet banking support, or connecting with a customer care executive.

This project has been created as part of the VITyarthi CSE Project.

Objectives

The main objectives of this project are:

To create a simple bank customer support system.
To understand the use of functions in Python.
To implement if-elif-else conditions.
To use while loops for interactive menus.
To take input from the user.
To create a simple IVR-style menu system.
To understand how different menu options can perform different tasks.
To provide a basic simulation of a banking helpline.
 Technologies Used
Programming Language: Python
Modules Used:
time
sys

No external libraries are required to run this project.

 Features
1. Language Selection

When the program starts, the user is presented with three options:

---Language Selection---

1. For English
2. For Other Language
3. Exit

The user can select English, choose the other-language option, or exit the system.

2. Account Balance

The user can select the account balance option from the main menu.

Example:

Your current bank account balance is 2,50,000 rupees only
3. Lost or Stolen Debit Card

The system provides an option for blocking a lost or stolen debit card.

The program displays a message explaining that the card will be blocked after verification.

4. Loan and Internet Banking Support

This option provides a submenu containing:

a) Home Loan
b) Reset Net Banking Password

The user can select either option to receive the corresponding support message.

5. Customer Care Executive

The user can choose to connect with a customer care executive.

The program simulates a short waiting period before connecting the customer.

6. Exit / Go Back

The user can exit the program from the language-selection menu or return to the language-selection process from the main menu.

 Project Structure

A simple project structure can be:

VITyarthi-CSE-Project/
└── README.md

Where:

apex_bank.py → Main Python program
README.md → Project documentation
 How to Run the Project
Step 1: Install Python

Make sure Python is installed on your computer.

You can check it using:

python --version


Step 2: Save the Python File

Save the project code in a file named:

CseProject.py
Step 3: Open Terminal / Command Prompt

Navigate to the folder containing the Python file.

Step 4: Run the Program

Use:

python CseProject.py


 Sample Output
[SYSTEM] : Welcome to the Apex Support

---Language Selection---
1. For English
2. For Other Language
3. Exit

Please press the option (1-3): 1

English Language has been chosen

========= MAIN MENU ==========
1. Account Balance
2. Block a Lost or Stolen Debit Card
3. Loan and Internet Banking Support
4. Speak with Customer Care Executive
0. Go Back to the Language selection

Enter Your Option: 1

Your current bank account balance is 2,50,000 rupees only
 Program Flow

The basic flow of the program is:

Start
  |
  v
Welcome Message
  |
  v
Language Selection
  |
  +----> English
  |        |
  |        v
  |    Main Menu
  |        |
  |        +----> Account Balance
  |        |
  |        +----> Block Debit Card
  |        |
  |        +----> Loan / Internet Banking
  |        |
  |        +----> Customer Care Executive
  |        |
  |        +----> Go Back
  |
  +----> Other Language
  |        |
  |        v
  |   Currently Unavailable
  |
  +----> Exit
           |
           v
          End
 Python Concepts Used

This project demonstrates several basic Python programming concepts.

Functions

The project uses functions such as:

def speak_and_print(text):

and:

def customer_care_helpline():
Conditional Statements

The program uses:

if
elif
else

to process different user choices.

Loops

while True is used to keep the menu running until the user exits or moves to another section.

User Input

The input() function is used to receive choices from the user.

Example:

language_choice = input("Please press the option (1-3) : ")
Modules

The project uses the built-in Python modules:

import time
import sys

The time module is used to create delays, while sys is used to exit the program.

