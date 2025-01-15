Feature: Command logout

    Scenario: User logout of your account
        Given the user is logged into the system
        When the user enters "logout" or the number 3
        Then the system returns to the login prompt, without terminating the system