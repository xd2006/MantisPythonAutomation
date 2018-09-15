import random

from fixture.application import Application
from model.project import Project


def test_add_project(app: Application):
    app.session.ensure_logon()

    index = random.randrange(100)
    status = random.choice(['development', 'release', 'stable', 'obsolete'])
    view_status = random.choice(['public', 'private'])

    project = Project(name="Test name {}".format(index), description="Test desc {}".format(index), status=status,
                      view_status=view_status)
    old_list = app.soap.get_projects()

    app.projects.add_project(project)

    new_list = app.soap.get_projects()

    old_list.append(project)

    assert sorted(old_list) == sorted(new_list)