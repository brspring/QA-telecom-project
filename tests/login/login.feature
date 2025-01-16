Feature: User Login

    Scenario: Successful login
        Given the user is on the login screen
        When the user enters "admin" as login
        And enters "admin" as password
        Then the user is authenticated in the system
        And choose an option from the menu

    Scenario: Unsuccessful login with empty fields
        Given the login screen is displayed
        When the user submits an empty username and/or password
        Then the system should display "Username and password cannot be empty"
        And remain on the login screen

    Scenario: Unsuccessful login with incorrect credentials
        Given the user is on the login screen
        When enter a username and password that are not in the file "logins.txt"
        Then the user should see "Incorrect login credentials, please try again!"
        And remain on the login screen