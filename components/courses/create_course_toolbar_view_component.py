from playwright.sync_api import Page
from elements.text import Text
from elements.button import Button
from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page, 'create-course-toolbar-title-text', 'Create Course Title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create Course Button')

    def check_visible(self, mis_create_course_disabled=True):
        self.create_course_title.check_visible()
        if mis_create_course_disabled:
            self.create_course_button.check_disabled()
        if not mis_create_course_disabled:
            self.create_course_button.check_enabled()
            self.create_course_button.click()
