import time
from selenium.webdriver.common.by import By


class SearchPage:
    search_box_xpath = "//input[@type='search']"
    table_row_xpath = "//table[@id='task-table']/tbody/tr"

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def search(self):
        search_box = self.driver.find_element(By.XPATH, self.search_box_xpath)
        time.sleep(5)
        search_box.send_keys("New York")
        assert search_box.is_displayed(), "Search box is not visible!"
        time.sleep(5)
