from selenium.webdriver.common.by import By

#class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTRATION_INPUT_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTRATION_INPUT_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTRATION_INPUT_SUBMIT_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTRATION_BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BUSKET_BTN = (By.CSS_SELECTOR, " .btn-add-to-basket")
    MSG_PRODUCT_ADD_BUSKET = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    MSG_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert .alertinner p strong")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_LINK = (By.XPATH, "//a[text()='View basket']")
    MSG_EMPTY_BASKET = (By.XPATH, "//p[contains(text(),'Your basket is empty.')]")