import allure
@allure.step("opening browser")
def open_browser():
    with allure.step("Get browser"):
        ...
    with allure.step("Start browser"):
        ...
@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    ...

@allure.step("Close browser")
def close_browser():
    ...
def test_feature():
    open_browser()
    create_course(title="locust")
    create_course(title="Pytest")
    create_course(title="Python")
    close_browser()