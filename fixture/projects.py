from fixture.general import GeneralHelper
from model.project import Project


class ProjectsHelper(GeneralHelper):

    def __init__(self, app):
        super().__init__(app)

    def get_projects_list(self):
        projects = []
        wd = self.app.wd

        self.navigate_to_manage_projects()

        rows = wd.find_elements_by_xpath("//table[@class='width100']//tr[@class='row-1' or @class='row-2']")
        for row in rows:
            cells = row.find_elements_by_css_selector("td")
            name = cells[0].find_element_by_css_selector("a").text
            status = cells[1].text
            view_status = cells[3].text
            description = cells[4].text
            projects.append(Project(name=name, status=status, view_status=view_status,
                                    description=description))
        return projects

    def add_project(self, project):
        self.navigate_to_manage_projects()
        self.click_create_new_project()
        self.populate_new_project_form(project)
        self.click_add_project()
        self.click_proceed()

    def navigate_to_manage_projects(self):
        wd = self.app.wd
        if "manage" not in wd.current_url:
            wd.find_element_by_xpath("//td/a[.='Manage']").click()
        if len(wd.find_elements_by_xpath("//td[@class='form-title'][contains(.,'Projects')]")) == 0:
            wd.find_element_by_xpath("//p/span[contains(.,'Manage Projects')]/a").click()

    def click_create_new_project(self):
        wd = self.app.wd
        if "manage_proj_create_page" not in wd.current_url:
            wd.find_element_by_css_selector("input[value='Create New Project']").click()

    def populate_new_project_form(self, project):
        self.populate_by_name('name', project.name)
        self.populate_by_name('description', project.description)
        self.select_by_name('status', project.status)
        self.select_by_name('view_state', project.view_status)

    def click_add_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def click_proceed(self):
        wd = self.app.wd
        try:
            wd.find_element_by_xpath("//a[contains(.,'Proceed')]").click()
        except:
            # redirect was already performed
            pass
