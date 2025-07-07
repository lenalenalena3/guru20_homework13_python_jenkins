from selene import browser, have


class LeftPanel:
    def get_elements_icon(self, header_text):
        return browser.element(f'//div[text()="{header_text}"]//following-sibling::*//div[@class="icon"]')

    def get_menu_list_item(self, item):
        return browser.element(f'//div[contains(@class,"element-list collapse")]//span[text()="{item}"]')

    def open(self, element, item):
        browser.open('/text-box')

        menu_item = self.get_menu_list_item(item).element('./ancestor::div[1]')
        if not menu_item.matching(have.css_class("show")):
            self.get_elements_icon(element).click()
        self.get_menu_list_item(item).click()

    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')