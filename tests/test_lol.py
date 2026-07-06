import pytest
from playwright.sync_api import expect, Page


test_data = [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password1"),
]

@pytest.mark.parametrize(
    "email, password",
    test_data
)


@pytest.mark.regression
@pytest.mark.authorization
def test_test_ru(chromium_page: Page, email: str, password: str):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(email)

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(password)

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
    chromium_page.wait_for_timeout(500)
