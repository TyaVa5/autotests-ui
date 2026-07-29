import pytest
import allure
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic


@pytest.mark.dashboard
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
class TestDashboard:

    @allure.title("Check displaying of dashboard page")
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        # Добавили проверку Navbar компонента на странице Dashboard
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible("username")
        dashboard_page_with_state.dashboard_toolbar.check_visible()
        dashboard_page_with_state.check_visible()
