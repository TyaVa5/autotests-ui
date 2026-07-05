import pytest

from playwright.sync_api import Playwright, Page, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state :Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    header_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(header_courses).to_be_enabled()
    expect(header_courses).to_have_text("Courses")

    body_icon_courses_empty = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(body_icon_courses_empty).to_be_enabled()
    expect(body_icon_courses_empty).to_be_visible()

    body_courses_header_empty = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(body_courses_header_empty).to_be_enabled()
    expect(body_courses_header_empty).to_have_text("There is no results")

    body_courses_text_empty = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(body_courses_text_empty).to_be_enabled()
    expect(body_courses_text_empty).to_have_text("Results from the load test pipeline will be displayed here")