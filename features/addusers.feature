Feature: AddUsers

    Scenario Outline: Navigate to User List Table
        Given I load the website
        When I go to "User List Table" page
        Then I see this component "<rows>"
        Examples:
            | rows              |
            | Status            |
            | Detector Settings |
            | Battery           |
            | GPS               |

    Scenario Outline: Add a user
        Given I go to the "User List Table" page
        When I add a user
        Then The table shows correct values for row "<rows>"
        Examples:
            | rows                    |
            | Status                  |
            | White Reference Count   |
            | Collect Reference Count |
            | Dark Reference Count    |
            | Last White Reference    |
            | Last Optimize           |
            | Last Dark Reference     |
            | Last Wavelength Check   |

    Scenario: Users are unique
        Given I load the website
        When I go to "Dashboard" page
        Then Clicking on Status Refresh should refresh status component

