Feature: User Login

    Scenario: Successful login
        Given the user is on the login screen
        When the user enters "admin" as login
        And enters "admin" as password
        Then the user is authenticated in the system and can choose an option from the menu

    Scenario: Unsuccessful login with incorrect credentials
        Given the user is on the login screen
        When enter a username and password that are not in the file "logins.txt"
        Then the user should see "Incorrect login credentials, please try again!"
