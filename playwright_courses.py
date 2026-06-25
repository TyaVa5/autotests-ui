from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_enabled()
    registration_email_input.focus()
    for registration_email in "user.name@gmail.com":
        page.keyboard.press(registration_email, delay=50)

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(registration_username_input).to_be_enabled()
    registration_username_input.focus()
    for registration_username in "username":
        page.keyboard.press(registration_username, delay=50)

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_enabled()
    registration_password_input.focus()
    for registration_password in "password":
        page.keyboard.press(registration_password, delay=50)

    expect(registration_button).not_to_be_disabled()
    registration_button.click()

    context.storage_state(path="browser-state-authorize.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state-authorize.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    page.wait_for_timeout(1000)

    header_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(header_courses).to_be_enabled()
    expect(header_courses).to_have_text("Courses")

    body_icon_courses_empty = page.get_by_test_id('courses-list-empty-view-icon')
    expect(body_icon_courses_empty).to_be_enabled()

    body_courses_header_empty = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(body_courses_header_empty).to_be_enabled()
    expect(body_courses_header_empty).to_have_text("There is no results")

    body_courses_text_empty = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(body_courses_text_empty).to_be_enabled()
    expect(body_courses_text_empty).to_have_text("Results from the load test pipeline will be displayed here")
    page.wait_for_timeout(1000)



