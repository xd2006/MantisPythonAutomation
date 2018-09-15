from fixture.general import GeneralHelper


class SessionHelper(GeneralHelper):

    def __init__(self, app):
        super().__init__(app)

    def logon(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[.='Logout']").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//a[.='Logout']")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username


    def ensure_logon(self, username=None, password=None):
        if username is None or password is None:
            username = self.app.user
            password = self.app.password

        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.logon(username, password)

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//td[contains(.,'Logged in as')]/span").text
