import allure
from allure_commons.types import Severity

from demoga_tests.data import users_simpl
from demoga_tests.model.application import app

@allure.severity(Severity.NORMAL)
@allure.label("owner", "tinkalyuk")
@allure.link("https://demoqa.com", name="demoqa.com")
@allure.title("Форма сокращенной регистрации")
@allure.description("Заполнение формы регистрации, отправка и проверка результата заполнения")
def test_simple_forms_filling_and_submit(setup_browser):
    student = users_simpl.student_simpl
    with allure.step("Открытие страницы"):
        app.left_panel.open_simple_registration_form()
    with allure.step(f"Заполнение формы {student}"):
        app.registration_simple_page.register(student)
    with allure.step(f"Проверка результата {student}"):
        app.registration_simple_page.should_have_registered(student)