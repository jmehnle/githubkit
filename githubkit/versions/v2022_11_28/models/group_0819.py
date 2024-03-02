"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0014 import AppPermissions


class AppInstallationsInstallationIdAccessTokensPostBody(GitHubModel):
    """AppInstallationsInstallationIdAccessTokensPostBody"""

    repositories: Missing[List[str]] = Field(
        default=UNSET,
        description="List of repository names that the token should have access to",
    )
    repository_ids: Missing[List[int]] = Field(
        default=UNSET,
        description="List of repository IDs that the token should have access to",
    )
    permissions: Missing[AppPermissions] = Field(
        default=UNSET,
        title="App Permissions",
        description="The permissions granted to the user access token.",
    )


model_rebuild(AppInstallationsInstallationIdAccessTokensPostBody)

__all__ = ("AppInstallationsInstallationIdAccessTokensPostBody",)
