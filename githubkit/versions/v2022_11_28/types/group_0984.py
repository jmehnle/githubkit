"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict


class ReposOwnerRepoCheckSuitesPostBodyType(TypedDict):
    """ReposOwnerRepoCheckSuitesPostBody"""

    head_sha: str


__all__ = ("ReposOwnerRepoCheckSuitesPostBodyType",)
