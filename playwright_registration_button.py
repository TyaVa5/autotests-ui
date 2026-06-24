from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()
    page.wait_for_timeout(1000)

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_enabled()
    registration_email_input.focus()
    for email_character in "user.name@gmail.com":
        page.keyboard.type(email_character, delay=100)
    page.wait_for_timeout(1000)

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(registration_username_input).to_be_enabled()
    registration_username_input.focus()
    for username_character in "username":
        page.keyboard.type(username_character, delay=100)
    page.wait_for_timeout(1000)

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_enabled()
    registration_password_input.focus()
    for password_character in "password":
        page.keyboard.type(password_character, delay=100)
    page.wait_for_timeout(1000)

    expect(registration_button).not_to_be_disabled()
    page.wait_for_timeout(1000)

