Feature: Main menu

    Scenario: User enters an invalid command
        Given the user is logged into the system
        When the user enters anything that is not one of the possible options
        Then the system should display the message:
            "Unknown command! try the commands below."

    Scenario: User enters an empty command
        Given the user is logged into the system
        When the user presses "Enter" without typing any command
        Then the system should display the message:
            "No command was typed, please type a command."

    Scenario: User enters a valid command with mixed case letters
        Given the user is logged into the system
        When the user enters a command using mixed case letters "ShOw InTeRfAcEs"
        Then the system should interpret the command normally
        
    Scenario: User logout of your account
        Given the user is logged into the system
        When the user enters "logout" or the number 3
        Then the system returns to the login prompt, without terminating the system

    Scenario: User exit the system
        Given the user is logged into the system
        When the user enters "exit" or the number 4
        Then the system exits and returns to the main shell prompt

    Scenario: User interrupts the program
        Given the user is logged into the system
        When the user presses "Ctrl+C"
        Then the system displays "Program interrupted by user. Exiting the system."
        And the system exits and returns to the main shell prompt