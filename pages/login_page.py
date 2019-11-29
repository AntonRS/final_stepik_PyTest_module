from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Incorrect url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login from is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register link is not presented"

    def register_new_user(self, email, password):
        #  Go to the login / registration page
        self.go_to_login_page()
        # Find the email form and fill it out
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_EMAIL)
        input_email.send_keys(email)
        # Find the password form and fill it
        input_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_PASSWORD)
        input_password.send_keys(password)
        # Find the password confirmation form and fill it out
        input_submit_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_SUBMIT_PASSWORD)
        input_submit_password.send_keys(password)
        # Find the Register button and click it
        submit_registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_SUBMIT)
        submit_registration_button.click()