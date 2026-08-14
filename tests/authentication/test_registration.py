import pytest
import allure
from allure_commons.types import Severity
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.tags import AllureTag
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.routes import AppRoute
from config import settings


@pytest.mark.regression
@pytest.mark.registration
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
class TestRegistration:

    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.xdist_group(name="authorization-group")
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.check_visible(email = "", password = "", username = "")
        registration_page.registration_form.fill(settings.test_user.email, settings.test_user.password, settings.test_user.username)
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar.check_visible()