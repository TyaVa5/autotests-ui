import pytest
from playwright.sync_api import Playwright, Page, expect
from pygments.lexers import yang


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_enabled()
    registration_email_input.focus()
    for registration_email in "user.name1@gmail.com":
        page.keyboard.press(registration_email, delay=40)

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(registration_username_input).to_be_enabled()
    registration_username_input.focus()
    for registration_username in "username":
        page.keyboard.press(registration_username, delay=40)

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_enabled()
    registration_password_input.focus()
    for registration_password in "password":
        page.keyboard.press(registration_password, delay=40)

    expect(registration_button).not_to_be_disabled()
    registration_button.click()

    context.storage_state(path="browser-state.json")
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()

