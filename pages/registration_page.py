from pages.base_page import BasePage
from components.base_component import BaseComponent
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.link import Link
from elements.button import Button
import re
class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)
        self.base_component = BaseComponent(page)
        self.registration_button = Button(page,'registration-page-registration-button', 'Registration')
        self.login_link = Link(page, 'registration-page-login-link', 'Login')

    def click_registration_button(self):
        self.registration_button.check_enabled()
        self.registration_button.click()
        self.base_component.check_current_url(re.compile(".*/#/dashboard"))

    def click_login_link(self):
        self.login_link.check_visible()
        self.login_link.click()
