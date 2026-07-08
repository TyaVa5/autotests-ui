from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.check_dashboard_main_title = page.get_by_test_id('dashboard-toolbar-title-text')
        self.check_students_widget_title = page.get_by_test_id('students-widget-title-text')
        self.check_courses_widget_title = page.get_by_test_id('courses-widget-title-text')
        self.check_activities_widget_title = page.get_by_test_id('activities-widget-title-text')
        self.check_scores_widget_title = page.get_by_test_id('scores-widget-title-text')


    def check_visible_dashboard_main_title(self):
        expect(self.check_dashboard_main_title).to_be_visible()
        expect(self.check_dashboard_main_title).to_have_text("Dashboard")

    def check_visible_students_widget_title(self):
        expect(self.check_students_widget_title).to_be_visible()
        expect(self.check_students_widget_title).to_have_text("Students")

    def check_visible_courses_widget_title(self):
        expect(self.check_courses_widget_title).to_be_visible()
        expect(self.check_courses_widget_title).to_have_text("Courses")

    def check_visible_activities_widget_title(self):
        expect(self.check_activities_widget_title).to_be_visible()
        expect(self.check_activities_widget_title).to_have_text("Activities")

    def check_visible_scores_widget_title(self):
        expect(self.check_scores_widget_title).to_be_visible()
        expect(self.check_scores_widget_title).to_have_text("Scores")
