import typing as ty
from pydantic import BaseModel, Field, AliasChoices, HttpUrl
from datetime import date

ISSUE_FIELDS = [
    "assignees",
    "author",
    "body",
    "closed",
    "closedAt",
    "comments",
    "createdAt",
    "id",
    "isPinned",
    "labels",
    "milestone",
    "number",
    "projectCards",
    "projectItems",
    "reactionGroups",
    "state",
    "stateReason",
    "title",
    "updatedAt",
    "url",
]

ISSUE_FIELDS_DEFAULT = [
    "author",
    "title",
    "url",
    "body"
]

class Issue:
    pass

class ProjectBase(BaseModel):
    # these are taken straight from GH
    closed: bool
    id: str
    number: int
    public: bool
    readme: str # long
    short_description: str = Field(None, validation_alias=AliasChoices("short_description", "shortDescription"))
    title: str
    url: HttpUrl

class ProjectExtra(BaseModel):
    start: ty.Optional[date] = Field(None, validation_alias=AliasChoices("start", "start date"))
    end: ty.Optional[date] = Field(None, validation_alias=AliasChoices("end", "end date"))
    project_number: ty.Optional[int] = None
    work_types: list[str] = []
    project_drivers: list[str] = []
    director: str # replace with project roles...
    stakeholders: ty.Optional[list[str]] = None
    delivery: ty.Optional[list[str]] = None


class Project(ProjectBase, ProjectExtra):
    pass