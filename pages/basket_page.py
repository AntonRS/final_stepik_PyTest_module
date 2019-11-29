from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasketPage(BasePage):
    def should_be_empty_basket_msg(self):
        assert self.is_element_present(*BasePageLocators.MSG_EMPTY_BASKET), "Message about empty basket is not presented"

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasePageLocators.MSG_EMPTY_BASKET), \
        "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_empty_basket_message_disappeared(self):
        assert self.is_disappeared(*BasePageLocators.MSG_EMPTY_BASKET), \
        "Success message is not disappeared, but should be"