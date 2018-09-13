from selenium.webdriver.support.select import Select


class GeneralHelper:
    def __init__(self, app):
        from fixture.application import Application
        self.app: Application = app

    def populate_by_name(self, name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(name).click()
            wd.find_element_by_name(name).clear()
            wd.find_element_by_name(name).send_keys(text)

    def select_by_name(self, name, text):
        if text is not None:
            wd = self.app.wd
            select_element: Select = Select(wd.find_element_by_name(name))
            select_element.select_by_visible_text(text)