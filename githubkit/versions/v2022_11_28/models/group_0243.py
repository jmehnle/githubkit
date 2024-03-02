"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class GitCommit(GitHubModel):
    """Git Commit

    Low-level Git commit operations within a repository
    """

    sha: str = Field(description="SHA for the commit")
    node_id: str = Field()
    url: str = Field()
    author: GitCommitPropAuthor = Field(
        description="Identifying information for the git-user"
    )
    committer: GitCommitPropCommitter = Field(
        description="Identifying information for the git-user"
    )
    message: str = Field(description="Message describing the purpose of the commit")
    tree: GitCommitPropTree = Field()
    parents: List[GitCommitPropParentsItems] = Field()
    verification: GitCommitPropVerification = Field()
    html_url: str = Field()


class GitCommitPropAuthor(GitHubModel):
    """GitCommitPropAuthor

    Identifying information for the git-user
    """

    date: datetime = Field(description="Timestamp of the commit")
    email: str = Field(description="Git email address of the user")
    name: str = Field(description="Name of the git user")


class GitCommitPropCommitter(GitHubModel):
    """GitCommitPropCommitter

    Identifying information for the git-user
    """

    date: datetime = Field(description="Timestamp of the commit")
    email: str = Field(description="Git email address of the user")
    name: str = Field(description="Name of the git user")


class GitCommitPropTree(GitHubModel):
    """GitCommitPropTree"""

    sha: str = Field(description="SHA for the commit")
    url: str = Field()


class GitCommitPropParentsItems(GitHubModel):
    """GitCommitPropParentsItems"""

    sha: str = Field(description="SHA for the commit")
    url: str = Field()
    html_url: str = Field()


class GitCommitPropVerification(GitHubModel):
    """GitCommitPropVerification"""

    verified: bool = Field()
    reason: str = Field()
    signature: Union[str, None] = Field()
    payload: Union[str, None] = Field()


model_rebuild(GitCommit)
model_rebuild(GitCommitPropAuthor)
model_rebuild(GitCommitPropCommitter)
model_rebuild(GitCommitPropTree)
model_rebuild(GitCommitPropParentsItems)
model_rebuild(GitCommitPropVerification)

__all__ = (
    "GitCommit",
    "GitCommitPropAuthor",
    "GitCommitPropCommitter",
    "GitCommitPropTree",
    "GitCommitPropParentsItems",
    "GitCommitPropVerification",
)
