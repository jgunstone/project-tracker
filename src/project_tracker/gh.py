import subprocess
import json
from .models import ISSUE_FIELDS_DEFAULT

PROJECT_NUMBER = 1
OWNER = "jgunstone"
REPO = "project-tracker"
ISSUE_NUMBER = 1

STATUS = "gh auth status"
PROJECT_VIEW = "gh project view {project_number} --owner {owner} --format json"  # gh project view 12 --owner maxfordham --format json
PROJECT_ITEMS = "gh project item-list {project_number} --owner {owner} --format json --limit {limit}"
ISSUE = "gh issue view {number} --json {json_fields} --repo {owner}/{repo}"


def is_logged_in():
    check = subprocess.call(STATUS.split(" "))
    if check == 0:
        return True
    else:
        return False
    
def subprocess_capture_output(cmd: str)-> dict:
    completed_process = subprocess.run(cmd, shell=True, capture_output=True)
    return json.loads(completed_process.stdout.decode('utf-8'))

def project_item_list_cmd(project_number, owner=OWNER, limit=1000):
    return PROJECT_ITEMS.format(project_number=project_number, owner=owner, limit=limit)

def project_view_cmd(project_number, owner=OWNER):
    return PROJECT_VIEW.format(project_number=project_number, owner=owner)

def issue_cmd(number, repo, owner=OWNER, json_fields=ISSUE_FIELDS_DEFAULT):
    if json_fields is None:
        issue = ISSUE.replace("--json {json_fields} ", "")
        return issue.format(number=number, owner=owner, repo=repo)
    else:
        return ISSUE.format(number=number, json_fields=",".join(json_fields), owner=owner, repo=repo)

def get_project_item_list(project_number, owner=OWNER, limit=1000):
    
    cmd = project_item_list_cmd(project_number=project_number, owner=owner, limit=limit)
    data = subprocess_capture_output(cmd)

    return data

def get_milestones_from_item_list(data: dict, top=""):
    milestones = [
        d["milestone"] | {"id": d["id"]}
        for d in data["items"]
        if "milestone" in d.keys()
    ]
    milestones = list({v["title"]: v for v in milestones}.values())  # unique milestones

    # df_milestones = pd.DataFrame(milestones)
    # if len(df_milestones) > 0:
    #     df_milestones["end"] = df_milestones.dueOn.str.split("T", expand=True)[0]
    #     df_milestones["milestone"] = df_milestones["title"]
    #     del df_milestones["dueOn"]
    #     del df_milestones["description"]
    #     df_milestones["title"] = top

    return milestones

def get_project_milestones(project_number, owner=OWNER, limit=1000):
    return get_milestones_from_item_list(get_project_item_list(project_number, owner=owner, limit=limit))

def get_project_view(project_number, owner=OWNER):

    cmd = project_view_cmd(project_number, owner=owner)
    data = subprocess_capture_output(cmd)

    return data

def get_issue(number, repo, owner=OWNER, json_fields=ISSUE_FIELDS_DEFAULT):

    cmd = issue_cmd(number, repo, owner=owner, json_fields=json_fields)
    data = subprocess_capture_output(cmd)

    return data
        
