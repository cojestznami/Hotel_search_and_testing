import logging

from selenium.webdriver.common.by import By


class SearchHotelPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "/html/body/div[17]/div/input"
        self.location_match_xpath = "//span[text()='Dubai']"
        self.check_in_input_name = "checkin"
        self.check_out_input_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath = "//button[text()=' Search']"
        self.logger = logging.getLogger(__name__)

    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element(By.XPATH, self.search_hotel_span_xpath).click()
        self.driver.find_element(By.XPATH, self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, self.location_match_xpath).click()

    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting check in [checkin] and [checkout] dates".format(checkin=check_in, checkout=check_out))
        self.driver.find_element(By.NAME, self.check_in_input_name).send_keys("check_in")
        self.driver.find_element(By.NAME, self.check_out_input_name).send_keys("check_out")

    def set_travellers(self, adults, child):
        self.logger.info("Setting travellers adults - {adults} and child - {kids}".format(adults=adults, kids=child))
        self.driver.find_element(By.ID, self.travellers_input_id).click()
        self.driver.find_element(By.ID, self.adult_input_id).clear()
        self.driver.find_element(By.ID, self.adult_input_id).send_keys(adults)
        self.driver.find_element(By.ID, self.child_input_id).clear()
        self.driver.find_element(By.ID, self.child_input_id).send_keys(child)

    def perform_search(self):
        self.logger.info("Performing search")
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
