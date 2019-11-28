from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BUSKET_BTN = (By.CSS_SELECTOR, " .btn-add-to-basket")
    MSG_PRODUCT_ADD_BUSKET = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    MSG_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert .alertinner p strong")