import re

from fixture.general import GeneralHelper





class SignupHelper(GeneralHelper):

    def __init__(self, app):
        super().__init__(app)

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get(self.app.base_url + "/signup_page.php")
        self.populate_by_name("username", username)
        self.populate_by_name("email", email)
        wd.find_element_by_css_selector("input[value='Signup']").click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmation_url(mail)
        wd.get(url)
        self.populate_by_name("password", password)
        self.populate_by_name("password_confirm", password)
        wd.find_element_by_css_selector("input[value='Update User']").click()

    def extract_confirmation_url(mail, text):
        re.search("http://.*$", text, re.MULTILINE).group(0)
