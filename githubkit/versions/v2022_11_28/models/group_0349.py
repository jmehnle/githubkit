"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class Key(GitHubModel):
    """Key

    Key
    """

    key: str = Field()
    id: int = Field()
    url: str = Field()
    title: str = Field()
    created_at: datetime = Field()
    verified: bool = Field()
    read_only: bool = Field()


model_rebuild(Key)

__all__ = ("Key",)
