"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union
from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0161 import SimpleCommit


class MergeGroup(GitHubModel):
    """Merge Group

    A group of pull requests that the merge queue has grouped together to be merged.
    """

    head_sha: str = Field(description="The SHA of the merge group.")
    head_ref: str = Field(description="The full ref of the merge group.")
    base_sha: str = Field(description="The SHA of the merge group's parent commit.")
    base_ref: str = Field(
        description="The full ref of the branch the merge group will be merged into."
    )
    head_commit: SimpleCommit = Field(title="Simple Commit", description="A commit.")


model_rebuild(MergeGroup)

__all__ = ("MergeGroup",)
