from playwright.sync_api import Page

from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesViewComponent
from components.courses.create_course_form_component import CreateCourseFormcomponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
        self.create_course_toolbar_view_component = CreateCourseToolbarViewComponent(page)
        self.create_course_form_component = CreateCourseFormcomponent(page)
        self.create_course_exercises_view_component = CreateCourseExercisesViewComponent(page)

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
