Feature: Command configure IP address

  Scenario: User configures the IP of an interface
    Given the user is logged into the system
    When the user enters "configure {valid_interface} ip {valid_ip}"
    Then the system configures the IP of the specified interface

  Scenario: User enters a non-existent interface
    Given the user is logged into the system
    When the user enters "configure {interface} ip {valid_ip}"
    And the interface does not exist
    Then thesystem display the message:
      "The interface {nome_interface} doesn't exist."

  Scenario: User enters an invalid IP
    Given the user is logged into the system
    When the user enters "configure {interface} ip {ip}"
    And the IP is invalid
    Then the system returns the error message "Invalid IP address."

  Scenario: User enters an incorrect keyword in the command
    Given the user is logged into the system
    When the user enters "{wrong_keyword} {interface} ip {ip}"
    Then the system display the message:
      "Invalid command format. Use: configure <interface-name> ip <ip-address/mask>"

  Scenario: Unexpected error occurs during IP configuration
    Given the user is logged into the system
    When the user enters "configure {interface} ip {ip}"
    And an unexpected error occurs
    Then the system returns the error message "Unexpected error: {error_message}" 

  Scenario: System fails to configure the IP
    Given the user is logged into the system
    When the user enters "configure {interface} ip {ip}"
    And an error occurs during the configuration
    Then the system returns the error message "Error configuring IP: {error_message}"