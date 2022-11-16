import logging
from selenium.webdriver.common.by import By


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
        self.hotel_prices_xpath = "//div[contains(@class, 'fs26')]//b"
        self.logger = logging.getLogger(__name__)

    def get_hotel_names(self):
        hotels = self.driver.find_elements(By.XPATH, self.hotel_names_xpath)
        names = [hotel.get_attribute("textContent") for hotel in hotels]
        self.logger.info("Available hotels are: ")

        for name in names:
            self.logger.info(name)
        return names

    def get_hotel_prices(self):
        prices = self.driver.find_elements(By.XPATH, self.hotel_prices_xpath)
        hotel_prices = [price.get_attribute("textContent") for price in prices]
        self.logger.info("Prices are: ")
        for price in hotel_prices:
            self.logger.info(price)
        return hotel_prices
