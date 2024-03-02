"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookIssuesLockedPropIssueAllof1(GitHubModel):
    """WebhookIssuesLockedPropIssueAllof1"""

    active_lock_reason: Union[
        None, Literal["resolved", "off-topic", "too heated", "spam"]
    ] = Field()
    assignee: Missing[Union[WebhookIssuesLockedPropIssueAllof1PropAssignee, None]] = (
        Field(default=UNSET)
    )
    assignees: Missing[
        List[Union[WebhookIssuesLockedPropIssueAllof1PropAssigneesItems, None]]
    ] = Field(default=UNSET)
    author_association: Missing[str] = Field(default=UNSET)
    body: Missing[Union[str, None]] = Field(default=UNSET)
    closed_at: Missing[Union[str, None]] = Field(default=UNSET)
    comments: Missing[int] = Field(default=UNSET)
    comments_url: Missing[str] = Field(default=UNSET)
    created_at: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    labels: Missing[
        List[Union[WebhookIssuesLockedPropIssueAllof1PropLabelsItems, None]]
    ] = Field(default=UNSET)
    labels_url: Missing[str] = Field(default=UNSET)
    locked: Literal[True] = Field()
    milestone: Missing[Union[WebhookIssuesLockedPropIssueAllof1PropMilestone, None]] = (
        Field(default=UNSET)
    )
    node_id: Missing[str] = Field(default=UNSET)
    number: Missing[int] = Field(default=UNSET)
    performed_via_github_app: Missing[
        Union[WebhookIssuesLockedPropIssueAllof1PropPerformedViaGithubApp, None]
    ] = Field(default=UNSET)
    reactions: Missing[WebhookIssuesLockedPropIssueAllof1PropReactions] = Field(
        default=UNSET
    )
    repository_url: Missing[str] = Field(default=UNSET)
    state: Missing[str] = Field(default=UNSET)
    timeline_url: Missing[str] = Field(default=UNSET)
    title: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user: Missing[WebhookIssuesLockedPropIssueAllof1PropUser] = Field(default=UNSET)


class WebhookIssuesLockedPropIssueAllof1PropAssignee(GitHubModel):
    """WebhookIssuesLockedPropIssueAllof1PropAssignee"""


class WebhookIssuesLockedPropIssueAllof1PropAssigneesItems(GitHubModel):
    """WebhookIssuesLockedPropIssueAllof1PropAssigneesItems"""


class WebhookIssuesLockedPropIssueAllof1PropLabelsItems(GitHubModel):
    """WebhookIssuesLockedPropIssueAllof1PropLabelsItems"""


class WebhookIssuesLockedPropIssueAllof1PropMilestone(GitHubModel):
    """WebhookIssuesLockedPropIssueAllof1PropMilestone"""


class WebhookIssuesLockedPropIssueAllof1PropPerformedViaGithubApp(GitHubModel):
    """WebhookIssuesLockedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssuesLockedPropIssueAllof1PropReactions(GitHubModel):
    """WebhookIssuesLockedPropIssueAllof1PropReactions"""

    plus_one: Missing[int] = Field(default=UNSET, alias="+1")
    minus_one: Missing[int] = Field(default=UNSET, alias="-1")
    confused: Missing[int] = Field(default=UNSET)
    eyes: Missing[int] = Field(default=UNSET)
    heart: Missing[int] = Field(default=UNSET)
    hooray: Missing[int] = Field(default=UNSET)
    laugh: Missing[int] = Field(default=UNSET)
    rocket: Missing[int] = Field(default=UNSET)
    total_count: Missing[int] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookIssuesLockedPropIssueAllof1PropUser(GitHubModel):
    """WebhookIssuesLockedPropIssueAllof1PropUser"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


model_rebuild(WebhookIssuesLockedPropIssueAllof1)
model_rebuild(WebhookIssuesLockedPropIssueAllof1PropAssignee)
model_rebuild(WebhookIssuesLockedPropIssueAllof1PropAssigneesItems)
model_rebuild(WebhookIssuesLockedPropIssueAllof1PropLabelsItems)
model_rebuild(WebhookIssuesLockedPropIssueAllof1PropMilestone)
model_rebuild(WebhookIssuesLockedPropIssueAllof1PropPerformedViaGithubApp)
model_rebuild(WebhookIssuesLockedPropIssueAllof1PropReactions)
model_rebuild(WebhookIssuesLockedPropIssueAllof1PropUser)

__all__ = (
    "WebhookIssuesLockedPropIssueAllof1",
    "WebhookIssuesLockedPropIssueAllof1PropAssignee",
    "WebhookIssuesLockedPropIssueAllof1PropAssigneesItems",
    "WebhookIssuesLockedPropIssueAllof1PropLabelsItems",
    "WebhookIssuesLockedPropIssueAllof1PropMilestone",
    "WebhookIssuesLockedPropIssueAllof1PropPerformedViaGithubApp",
    "WebhookIssuesLockedPropIssueAllof1PropReactions",
    "WebhookIssuesLockedPropIssueAllof1PropUser",
)
