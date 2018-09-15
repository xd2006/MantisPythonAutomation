from suds import WebFault
from suds.client import Client

from model.project import Project


def get_client():
    return Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")


class SoapHelper:
    def __init__(self, app):
        from fixture.application import Application
        self.app: Application = app

    def can_login(self, username, password):
        client = get_client()
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects(self, username=None, password=None):
        client = get_client()
        if username is None or password is None:
            username = self.app.user
            password = self.app.password

        projects = client.service.mc_projects_get_user_accessible(username, password)
        projects_list = []
        for p in projects:
            name = p['name']
            status = p['status']['name']
            view_state = p['view_state']['name']
            description = p['description']
            project = Project(name=name, status=status, view_status=view_state, description=description)
            projects_list.append(project)
        return projects_list
