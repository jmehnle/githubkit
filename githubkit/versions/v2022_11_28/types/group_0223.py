"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict, NotRequired


class ContributorType(TypedDict):
    """Contributor

    Contributor
    """

    login: NotRequired[str]
    id: NotRequired[int]
    node_id: NotRequired[str]
    avatar_url: NotRequired[str]
    gravatar_id: NotRequired[Union[str, None]]
    url: NotRequired[str]
    html_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    organizations_url: NotRequired[str]
    repos_url: NotRequired[str]
    events_url: NotRequired[str]
    received_events_url: NotRequired[str]
    type: str
    site_admin: NotRequired[bool]
    contributions: int
    email: NotRequired[str]
    name: NotRequired[str]


__all__ = ("ContributorType",)
