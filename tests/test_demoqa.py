import allure
from allure_commons.types import Severity

from demoga_tests.data import users
from demoga_tests.model.pages.registration_page import RegistrationPage


@allure.severity(Severity.NORMAL)
@allure.label("owner", "tinkalyuk")
@allure.link("https://demoqa.com", name="demoqa.com")
@allure.title("Форма регистрации")
@allure.description("Заполнение формы регистрации, отправка и проверка результата заполнения")
def test_forms_filling_and_submit(setup_browser):
    registration_page = RegistrationPage()
    student = users.student
    with allure.step("Открытие страницы"):
        registration_page.open()
    with allure.step(f"Заполнение формы {student}"):
        registration_page.register(student)
    with allure.step(f"Проверка результативной таблицы {student}"):
        registration_page.should_have_registered(student)