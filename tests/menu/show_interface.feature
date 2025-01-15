Feature: Command show interfaces

  Scenario: User lists interfaces
    Given the user is logged into the system
    When the user enters "show interfaces" or the number 1
    Then the system should display a list of network interfaces, with the header:
      Interface  IP Address      MAC Address        MTU   State


  Scenario: Interface has multiple IP addresses
    Given the user is logged into the system
    When the user enters "show interfaces" or the number 1
    And some interface has two IP addresses
    Then add a blank line below this interface with its second IP, as follows:
      Interface  IP Address      MAC Address        MTU   State
      eth0       192.167.0.20    00:2D:2A:4E:2E:3C  1500  UP
                 192.166.0.10

  Scenario: Interface has no IP address
    Given the user is logged into the system
    When the user enters "show interfaces" or the number 1
    Then the system should display "N/A" in the IP Address column for the interface:
      Interface  IP Address      MAC Address        MTU   State
      eth0       N/A             00:2D:2A:4E:2E:3C  1500  UP