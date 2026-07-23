
from components.base_component import BaseComponent
from elements.input import Input
from elements.button import Button
from elements.link import Link

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')
        self.username_input = Input(page,'registration-form-username-input', 'Username')
        self.registration_button = Button(page,'registration-page-registration-button', 'Registration')
        self.login_link = Link(page, 'registration-page-login-link', 'Login')

    def check_visible(self):
        self.email_input.check_visible()
        self.password_input.check_visible()
        self.username_input.check_visible()
        self.registration_button.check_disabled()
        self.login_link.check_visible()
        self.email_input.check_have_value("")
        self.password_input.check_have_value("")
        self.username_input.check_have_value("")

    def fill(self, email: str, password: str, username: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

        self.username_input.fill(username)
        self.username_input.check_have_value(username)


