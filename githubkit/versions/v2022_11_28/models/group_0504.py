"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookIssuesDemilestonedPropIssueAllof1(GitHubModel):
    """WebhookIssuesDemilestonedPropIssueAllof1"""

    active_lock_reason: Missing[Union[str, None]] = Field(default=UNSET)
    assignee: Missing[
        Union[WebhookIssuesDemilestonedPropIssueAllof1PropAssignee, None]
    ] = Field(default=UNSET)
    assignees: Missing[
        List[Union[WebhookIssuesDemilestonedPropIssueAllof1PropAssigneesItems, None]]
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
        List[Union[WebhookIssuesDemilestonedPropIssueAllof1PropLabelsItems, None]]
    ] = Field(default=UNSET)
    labels_url: Missing[str] = Field(default=UNSET)
    locked: Missing[bool] = Field(default=UNSET)
    milestone: Union[WebhookIssuesDemilestonedPropIssueAllof1PropMilestone, None] = (
        Field(
            title="Milestone",
            description="A collection of related issues and pull requests.",
        )
    )
    node_id: Missing[str] = Field(default=UNSET)
    number: Missing[int] = Field(default=UNSET)
    performed_via_github_app: Missing[
        Union[WebhookIssuesDemilestonedPropIssueAllof1PropPerformedViaGithubApp, None]
    ] = Field(default=UNSET)
    reactions: Missing[WebhookIssuesDemilestonedPropIssueAllof1PropReactions] = Field(
        default=UNSET
    )
    repository_url: Missing[str] = Field(default=UNSET)
    state: Missing[str] = Field(default=UNSET)
    timeline_url: Missing[str] = Field(default=UNSET)
    title: Missing[str] = Field(default=UNSET)
    updated_at: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)
    user: Missing[WebhookIssuesDemilestonedPropIssueAllof1PropUser] = Field(
        default=UNSET
    )


class WebhookIssuesDemilestonedPropIssueAllof1PropAssignee(GitHubModel):
    """WebhookIssuesDemilestonedPropIssueAllof1PropAssignee"""


class WebhookIssuesDemilestonedPropIssueAllof1PropAssigneesItems(GitHubModel):
    """WebhookIssuesDemilestonedPropIssueAllof1PropAssigneesItems"""


class WebhookIssuesDemilestonedPropIssueAllof1PropLabelsItems(GitHubModel):
    """WebhookIssuesDemilestonedPropIssueAllof1PropLabelsItems"""


class WebhookIssuesDemilestonedPropIssueAllof1PropMilestone(GitHubModel):
    """Milestone

    A collection of related issues and pull requests.
    """

    closed_at: Union[datetime, None] = Field()
    closed_issues: int = Field()
    created_at: datetime = Field()
    creator: Union[
        WebhookIssuesDemilestonedPropIssueAllof1PropMilestonePropCreator, None
    ] = Field(title="User")
    description: Union[str, None] = Field()
    due_on: Union[datetime, None] = Field()
    html_url: str = Field()
    id: int = Field()
    labels_url: str = Field()
    node_id: str = Field()
    number: int = Field(description="The number of the milestone.")
    open_issues: int = Field()
    state: Literal["open", "closed"] = Field(description="The state of the milestone.")
    title: str = Field(description="The title of the milestone.")
    updated_at: datetime = Field()
    url: str = Field()


class WebhookIssuesDemilestonedPropIssueAllof1PropMilestonePropCreator(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization", "Mannequin"]] = Field(
        default=UNSET
    )
    url: Missing[str] = Field(default=UNSET)


class WebhookIssuesDemilestonedPropIssueAllof1PropPerformedViaGithubApp(GitHubModel):
    """WebhookIssuesDemilestonedPropIssueAllof1PropPerformedViaGithubApp"""


class WebhookIssuesDemilestonedPropIssueAllof1PropReactions(GitHubModel):
    """WebhookIssuesDemilestonedPropIssueAllof1PropReactions"""

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


class WebhookIssuesDemilestonedPropIssueAllof1PropUser(GitHubModel):
    """WebhookIssuesDemilestonedPropIssueAllof1PropUser"""

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


model_rebuild(WebhookIssuesDemilestonedPropIssueAllof1)
model_rebuild(WebhookIssuesDemilestonedPropIssueAllof1PropAssignee)
model_rebuild(WebhookIssuesDemilestonedPropIssueAllof1PropAssigneesItems)
model_rebuild(WebhookIssuesDemilestonedPropIssueAllof1PropLabelsItems)
model_rebuild(WebhookIssuesDemilestonedPropIssueAllof1PropMilestone)
model_rebuild(WebhookIssuesDemilestonedPropIssueAllof1PropMilestonePropCreator)
model_rebuild(WebhookIssuesDemilestonedPropIssueAllof1PropPerformedViaGithubApp)
model_rebuild(WebhookIssuesDemilestonedPropIssueAllof1PropReactions)
model_rebuild(WebhookIssuesDemilestonedPropIssueAllof1PropUser)

__all__ = (
    "WebhookIssuesDemilestonedPropIssueAllof1",
    "WebhookIssuesDemilestonedPropIssueAllof1PropAssignee",
    "WebhookIssuesDemilestonedPropIssueAllof1PropAssigneesItems",
    "WebhookIssuesDemilestonedPropIssueAllof1PropLabelsItems",
    "WebhookIssuesDemilestonedPropIssueAllof1PropMilestone",
    "WebhookIssuesDemilestonedPropIssueAllof1PropMilestonePropCreator",
    "WebhookIssuesDemilestonedPropIssueAllof1PropPerformedViaGithubApp",
    "WebhookIssuesDemilestonedPropIssueAllof1PropReactions",
    "WebhookIssuesDemilestonedPropIssueAllof1PropUser",
)
