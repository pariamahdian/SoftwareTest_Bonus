Feature: Generate Model Functionality
  I want to verify the behavior of the generate_model function
    
  Scenario: Verify output for different working modes
    Given I have the following input objects
      | Characteristic | Blocks        |
      | 'A'            | ['a1', 'a2']  |
      | 'B'            | ['b1', 'b2']  |
      | 'C'            | ['c1', 'c2', 'c3'] |
      | 'D'            | ['d1', 'd2']  |
    When I enter the working mode <mode>
    Then the program should display the expected output based on the mode