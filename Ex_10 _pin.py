# PIN-CODE - 3 attempts, with counter (getpass to hide user input)
import getpass
# set supplied pin to empty string
supplied_pin = ""
# PIN set in string format to match user input type
PIN_number = "1234"
max_attempts = 3
# counter begins at one, and goes up after each guess
current_attempt = 1
# set loop to run while current_attempt is less than or same as max_attempts
while current_attempt <= max_attempts:
    # ask for user input to set value of supplied_pin (to re-set supplied_pin with each loop)
    # supplied_pin = input("Enter your PIN: ")
    supplied_pin = getpass.getpass("Enter your PIN: ")
    # in while loop, set condition for incorrect pin (user input doesn't match PIN)
    if supplied_pin != PIN_number:
        print("Attempt #", current_attempt, "incorrect")
        # increase counter by 1
        current_attempt = current_attempt + 1
    # in while loop, set condition for correct pin (user input matches PIN)
    else:
        print ("Attempt #",current_attempt, "Correct PIN!")
        # set counter to number more than max_attempts to exit while loop
        current_attempt = max_attempts + 1
# if condition for too many attempts
if supplied_pin != PIN_number:
    print("Too many attempts, your PIN is locked")