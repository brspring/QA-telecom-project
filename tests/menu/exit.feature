Feature: Command exit the system

    Scenario: User exit the system
        Given the user is logged into the system
        When the user enters "exit" or the number 4
        Then the system The system exits and returns to the main shell prompt