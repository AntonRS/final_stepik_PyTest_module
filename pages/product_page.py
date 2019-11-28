from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BTN)
        link.click()

    def save_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name
        
    def save_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        
    def should_be_product_page(self):
        self.should_be_added_to_basket()
        self.should_be_same_name(self.save_product_name())
        self.should_be_price_present()
        self.should_be_same_price(self.save_product_price())

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Incorrect url"

    def should_be_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MSG_PRODUCT_ADD_BUSKET), "Add to basket message from is not presented"

    def should_be_same_name(self, product_name):
        chk_name = self.browser.find_element(*ProductPageLocators.MSG_PRODUCT_ADD_BUSKET)
        text_chk_name = chk_name.text
        take_url = self.browser.current_url
        assert product_name == text_chk_name, f"Incorrect product name {text_chk_name} on {take_url}"

    def should_be_price_present(self):
        assert self.is_element_present(*ProductPageLocators.MSG_BASKET_TOTAL), "Total basket message not presented"

    def should_be_same_price(self, product_price):
        chk_total = self.browser.find_element(*ProductPageLocators.MSG_BASKET_TOTAL)
        text_chk_total = chk_total.text
        take_url = self.browser.current_url
        assert product_price == text_chk_total, f"Incorrect basket total {text_chk_total} on {take_url}"

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MSG_PRODUCT_ADD_BUSKET), \
        "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MSG_PRODUCT_ADD_BUSKET), \
        "Success message is not disappeared, but should be"