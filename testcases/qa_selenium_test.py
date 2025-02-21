import pytest

from PageObjects.Search import SearchPage
from Utilities.Baseclass import BaseClass
from Utilities.Readproperties import ReadConfig


class TestSearch(BaseClass):
    baseURL = ReadConfig.getApplicationURL()

    def setup_method(self):
        self.driver.get(self.baseURL)

    def test_search(self):
        search_page = SearchPage(self.driver)
        search_page.search()
