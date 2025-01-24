Feature: The studentinfo service back-end
    As a studentinfo Owner
    I need a RESTful catalog service
    So that I can keep track of all my studentinfo

Background:
    Given the following products
        | id     | name     
        | 100     | Jack
        | 101     | lak

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "stuidentinfo Catalog Administration" in the title
    And I should not see "404 Not Found"

Scenario: Create a Product
    When I visit the "Home Page"
    And I set the "id" to "100 and "101"
    And I set the "Name" to "jack" and "lak"
   And I press the "Create" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    Then the "Id" field should be empty
    And the "Name" field should be empty
    When I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see 100 in the id field
     And I should see "jack" in the "Name" 
         And I should see 101 in the id field
     And I should see "lak" in the "Name" field
  
