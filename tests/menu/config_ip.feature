Feature: Command configure IP address

  Scenario: User configures the IP of an interface
    Given the user is logged into the system
    When the user enters "configure {valid_interface} ip {valid_ip}"
    Then the system configures the IP of the specified interface

  Scenario: User enters a non-existent interface
    Given the user is logged into the system
    When the user enters "configure {interface} ip {valid_ip}"
    And the interface does not exist
    Then the system returns the error message "Error configuring IP: Cannot find device "{non_existent_interface_name}""

  Scenario: User enters an invalid IP
    Given the user is logged into the system
    When the user enters "configure {interface} ip {ip}"
    And the IP is invalid
    Then the system returns the error message "Invalid IP address."