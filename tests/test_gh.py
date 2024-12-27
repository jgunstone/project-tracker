from project_tracker.gh import (
    is_logged_in,
    get_project_item_list,
    get_project_milestones,
    get_project_view,
    get_issue,
    PROJECT_NUMBER,
    OWNER,
    REPO,
    ISSUE_NUMBER,
)
import pathlib
import json

FDIR_DOCS_DATA = pathlib.Path(__file__).parent.parent / "docs" / "data"



def test_check_status():
    result = is_logged_in()
    assert result


def test_get_project_item_list():  # requires mxf...
    data = get_project_item_list(PROJECT_NUMBER)
    fpth = FDIR_DOCS_DATA / "project-item-list.json"
    fpth.write_text(json.dumps(data, indent=4))
    assert isinstance(data, dict)

def test_get_project_milestones():
    data = get_project_milestones(PROJECT_NUMBER)

    fpth = FDIR_DOCS_DATA / "milestones.json"
    fpth.write_text(json.dumps(data, indent=4))
    assert isinstance(data, list)

def test_get_project_view():  # requires mxf...
    data = get_project_view(PROJECT_NUMBER)

    fpth = FDIR_DOCS_DATA / "project-view.json"
    fpth.write_text(json.dumps(data, indent=4))
    assert isinstance(data, dict)


def test_get_issue():  # requires mxf...
    data = get_issue(ISSUE_NUMBER, REPO, owner=OWNER)

    fpth = FDIR_DOCS_DATA / "issue.json"
    fpth.write_text(json.dumps(data, indent=4))
    assert isinstance(data, dict)

