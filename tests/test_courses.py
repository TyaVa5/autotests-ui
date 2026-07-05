import pytest

from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    print("Регистрируемся и авторизуемся")