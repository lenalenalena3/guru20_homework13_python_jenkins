from demoga_tests.model.pages.left_panel import LeftPanel
from demoga_tests.model.pages.registration_page import RegistrationPage
from demoga_tests.model.pages.registration_simple_page import RegistrationSimplePage

class Application:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.registration_simple_page = RegistrationSimplePage()
        self.left_panel = LeftPanel()

app = Application()