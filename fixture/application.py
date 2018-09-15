from selenium import webdriver

from fixture.james import JamesHelper
from fixture.mail import MailHelper
from fixture.projects import ProjectsHelper
from fixture.session import SessionHelper
from fixture.signup import SignupHelper


class Application:
    session: SessionHelper
    projects: ProjectsHelper
    wd: webdriver


    def __init__(self, browser, config):
        if (browser=="firefox"):
            self.wd = webdriver.Firefox(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files (x86)/Mozilla Firefox ESR/firefox.exe")
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser &s" % browser)
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.projects = ProjectsHelper(self)
        self.james = JamesHelper(self)
        self.base_url = config['web']['baseUrl']
        self.user = config['webadmin']['username']
        self.password = config['webadmin']['password']
        self.config = config

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
