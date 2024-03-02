"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgActionsSecretsGetResponse200Type(TypedDict):
    """OrgsOrgActionsSecretsGetResponse200"""

    total_count: int
    secrets: List[OrganizationActionsSecretType]


class OrganizationActionsSecretType(TypedDict):
    """Actions Secret for an Organization

    Secrets for GitHub Actions for an organization.
    """

    name: str
    created_at: datetime
    updated_at: datetime
    visibility: Literal["all", "private", "selected"]
    selected_repositories_url: NotRequired[str]


__all__ = (
    "OrgsOrgActionsSecretsGetResponse200Type",
    "OrganizationActionsSecretType",
)
