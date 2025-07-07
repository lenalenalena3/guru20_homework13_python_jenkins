from selene import browser, have


class RegistrationSimplePage:
    def __init__(self):
        self._full_name = browser.element('#userName')
        self._email = browser.element('#userEmail')
        self._current_address = browser.element('//textarea[@id="currentAddress"]')
        self._permanent_address = browser.element('//textarea[@id="permanentAddress"]')
        self.submit_button = browser.element('#submit')
        self._output_name = browser.element('#name')
        self._output_email = browser.element('#email')
        self._output_currentAddress = browser.element('#output').element('#currentAddress')
        self._output_permanentAddress = browser.element('#output').element('#permanentAddress')

    def register(self, user):
        self._full_name.type(user.name)
        self._email.type(user.email)
        self._current_address.type(user.current_address)
        self._permanent_address.type(user.permanent_address)
        browser.execute_script("arguments[0].scrollIntoView(true);", self.submit_button.locate())
        self.submit_button.click()

    def should_have_registered(self, user):
        self._output_name.should(have.text(f"Name:{user.name}"))
        self._output_email.should(have.text(f"Email:{user.email}"))
        self._output_currentAddress.should(have.text(f"Current Address :{user.current_address}"))
        self._output_permanentAddress.should(have.text(f"Permananet Address :{user.permanent_address}"))