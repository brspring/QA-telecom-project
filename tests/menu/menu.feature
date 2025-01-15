Feature: Main menu

    Scenario: User enters an invalid command
        Given the user is logged into the system
        When the user enters anything that is not one of the possible options
        Then the system should display "Unknown command! try the commands below."
