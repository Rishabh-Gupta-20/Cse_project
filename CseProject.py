
#                              VITyarthi CSE Project



                  
#                           Welcome to XYZ Bank Support 
                 


import time
import sys

def speak_and_print(text):
    """Print the output with slight delay"""
    print(f" [SYSTEM] : {text}")
    time.sleep(1.5)

def customer_care_helpline():
    speak_and_print("Welcome to the XYZ Bank Support")

    # Step 1 :Select the language
    while True:
        print("\n---Language Selection---")
        print("1. For English ")
        print("2. For Other Language ")
        print("3. Exit ")

        language_choice = input("Please press the option (1-3) : ")

        if language_choice == '1':
            current_language = "English"
            print("English Language has been chosen ")
        elif language_choice == '2':
            current_language = "Other"
            print("Other Language has been chosen ")
        elif language_choice == '3':
            print("Thank you for contacting in XYZ Bank. Have a Good Day")
            sys.exit()
        else:
            print("Invalid input. Please try again")

        # Step 2 :Main Customer Support Menu
        while True:
            if current_language == "English":
                print("\n========= MAIN MENU ==========")
                print("1. Account Balance ")
                print("2. Block a Lost or Stolen Debit Card")
                print("3. Loan and Internet Banking Support")
                print("4. Speak with Customer Care Executive")
                print("0. Go Back to the Language selection")

                choice = int(input("Enter Your Option : "))

                if choice == 1:
                    print("Your current bank account balance is 2,50,000 rupees only")
                elif choice == 2:
                    print("Your to secure your debit card Apex Bank will confirm OTP and and your debit card with number *123 will be blocked")
                elif choice ==  3:
                    # Sub menu 
                    print("\nLoan and Internet Banking")
                    print("a) Home Loan ")
                    print("b) Reset Net Banking Password ")
                    sub_choice = str(input("Enter option " ))
                    if sub_choice == "a":
                        print("Your home loan application is under review. You will receive an SMS update shortly.")
                    elif sub_choice == "b":
                        print("A password reset link has been sent to your registered email address.")
                    else:
                        print("Invalid sub option. Returning to the Main Menu")
                elif choice == 4:
                    print("Connecting your call to our Executive. Please Wait")
                    time.sleep(2)
                    print("Hello I am Ananat, Sir. How can I help you ?")
                    break
                elif choice == 0:
                    customer_care_helpline()   # Restarts whole process again
                    break
                else:
                    speak_and_print("Invalid key pressed. Please listen to the options carefully.")

            elif current_language == "Other":
                print("********** SORRY ***********")
                print("The system is currently unavailable for other languages")

            customer_care_helpline()



# Start the interactive script
if __name__ == "__main__":
    customer_care_helpline()



