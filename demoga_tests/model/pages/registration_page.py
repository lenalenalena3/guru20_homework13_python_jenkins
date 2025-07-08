import allure
from selene import browser, have
from selenium.webdriver import Keys

from demoga_tests.model import resource


class RegistrationPage:
    def __init__(self):
        self._should_have_registered = browser.element('//table').all('td')
        self._first_name = browser.element('#firstName')
        self._last_name = browser.element('#lastName')
        self._email = browser.element('#userEmail')
        self._gender = browser.element('#genterWrapper').all('label')
        self._mobile = browser.element('#userNumber')
        self._date_of_birth = browser.element('#dateOfBirthInput')
        self._date_of_birth_year = self._date_of_birth.element('//select[@class="react-datepicker__year-select"]')
        self._date_of_birth_month = self._date_of_birth.element('//select[@class="react-datepicker__month-select"]')
        self._date_of_birth_day = browser.all(
            '//div[contains(@class,"datepicker__day--") and not(contains(@class,"outside-month"))]')
        self._subjects = browser.element('#subjectsInput')
        self._subjects_elements = self._subjects.all('//div[contains(@id, "option")]')
        self._hobbies = browser.element('#hobbiesWrapper').all('//input/following-sibling::label')
        self._picture = browser.element('//input[@type="file"]')
        self._current_address = browser.element('#currentAddress')
        self._state = browser.element('#state')
        self._state_elements = self._state.all('//div[contains(@id, "option")]')
        self._city = browser.element('#city')
        self._city_elements = self._city.all('//div[contains(@id, "option")]')
        self._submit_button = browser.element('[id="submit"]')

    @allure.step(f"Открыть форму регистрации")
    def open(self):
        browser.open('/automation-practice-form')

    @allure.step("Заполнить first_name")
    def _fill_first_name(self, value):
        self._first_name.type(value)

    @allure.step("Заполнить last_name")
    def _fill_last_name(self, value):
        self._last_name.type(value)

    @allure.step("Заполнить email_name")
    def _fill_email(self, value):
        self._email.type(value)

    @allure.step("Выбрать gender")
    def _set_radio_gender(self, value):
        self._gender.element_by(have.text(value)).click()

    @allure.step("Заполнить mobile")
    def _fill_mobile(self, value):
        self._mobile.type(value)

    @allure.step("Заполнить date_of_birth")
    def _set_date_of_birth(self, date_of_birth):
        self._date_of_birth.click()
        self._date_of_birth_year.click()
        self._date_of_birth_year.all('option').element_by(have.text(str(date_of_birth.year))).click()
        self._date_of_birth_month.click()
        self._date_of_birth_month.all('option').element_by(have.text(date_of_birth.strftime('%B'))).click()
        self._date_of_birth_day.element_by(have.text(str(date_of_birth.day))).click()

    @allure.step("Заполнить subjects")
    def _set_subjects(self, value):
        browser.driver.execute_script("arguments[0].scrollIntoView(true);", self._submit_button.locate())
        self._subjects.set_value(value)
        self._subjects_elements.element_by(have.text(value)).click()

    @allure.step("Выбрать hobbies")
    def _set_checkbox_hobbies(self, value):
        self._hobbies.element_by(have.text(value)).click()

    @allure.step("Загрузить picture")
    def _upload_picture(self, value):
        self._picture.set_value(value)

    @allure.step("Заполнить current_address")
    def _fill_current_address(self, value):
        self._current_address.type(value)

    @allure.step("Заполнить state")
    def _set_state(self, value):
       # browser.driver.execute_script("arguments[0].scrollIntoView(true);", self._state.locate())
        self._state.click()
        self._state_elements.element_by(have.text(value)).click()

    @allure.step("Заполнить city")
    def _set_city(self, value):
        self._city.click()
        self._city_elements.element_by(have.text(value)).click()

    @allure.step("Нажать кнопку submit")
    def submit(self):
        self._submit_button.click()

    @allure.step("Заполнить форму регистрации данными пользователя")
    def register(self, user):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._set_radio_gender(user.gender)
        self._fill_mobile(user.mobile)
        self._set_date_of_birth(user.date_of_birth)
        self._set_subjects(user.subjects)
        self._set_checkbox_hobbies(user.hobbies)
        self._upload_picture(resource.path(user.picture))
        self._fill_current_address(user.current_address)
        self._set_state(user.state)
        self._set_city(user.city)
        self.submit()

    @allure.step("Проверить результирующую таблицу")
    def should_have_registered(self, user):
        year = str(user.date_of_birth.year)
        month = user.date_of_birth.strftime('%B')
        day = str(user.date_of_birth.day)

        self._should_have_registered.should(have.exact_texts(
            'Student Name', f"{user.first_name} {user.last_name}",
            'Student Email', user.email,
            'Gender', user.gender,
            'Mobile', user.mobile[:10],
            'Date of Birth', f"{day} {month},{year}",
            'Subjects', user.subjects,
            'Hobbies', user.hobbies,
            'Picture', user.picture,
            'Address', user.current_address,
            'State and City', f"{user.state} {user.city}"))