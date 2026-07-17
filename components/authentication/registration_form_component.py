import re
from components.base_component import BaseComponent
from playwright.sync_api import expect


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def check_visible(self):
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.username_input).to_be_visible()
        expect(self.registration_button).to_be_disabled()
        expect(self.login_link).to_be_visible()
        expect(self.email_input).to_have_value("")
        expect(self.password_input).to_have_value("")
        expect(self.username_input).to_have_value("")

    def fill(self, email: str, password: str, username: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)


    def click_registration_button(self):
        expect(self.registration_button).not_to_be_disabled()
        self.registration_button.click()
        self.check_current_url(re.compile(".*/#/dashboard"))

    def click_login_link(self):
        self.login_link.click()
        expect(self.login_link).to_be_enabled()


