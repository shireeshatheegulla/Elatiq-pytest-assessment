# Elatiq-pytest-assessment
Overview :

This project automates a web search functionality using Selenium WebDriver with pytest. It verifies the presence of a search box, performs a search operation, and validates that results are displayed correctly.

Approach:

WebDriver Initialization: Uses webdriver_manager to handle ChromeDriver installation automatically.

Test Execution:

Navigates to the target website.

Waits for the search box to be visible and clickable.

Enters a search query and validates the displayed results.

Assertions:

Ensures the search box is present and functional.

Confirms that search results appear after entering a query.

Test Reporting: Uses pytest for structured test execution and reporting.

Prerequisites : 

Python 3.7+

Google Chrome (Latest Version)

Required Python packages:

pip install selenium webdriver-manager pytest

How to Run the Script

Clone the Repository:

git clone [<repo-url>](https://github.com/shireeshatheegulla/Elatiq-pytest-assessment/edit/shireesha_pytest_assessmen)
cd Elatiq-pytest-assessment

Run the Test:
pytest --browser chrome ./testcases/qa_selenium_test.py
            or
pytest --browser edge ./testcases/qa_selenium_test.py  
            or
pytest testcases/qa_selenium_test.py --verbose

View Results:

Test results will be displayed in the console.
