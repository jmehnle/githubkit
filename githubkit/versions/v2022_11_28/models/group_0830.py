"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import Annotated

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class GistsGistIdCommentsPostBody(GitHubModel):
    """GistsGistIdCommentsPostBody"""

    body: str = Field(max_length=65535, description="The comment text.")


model_rebuild(GistsGistIdCommentsPostBody)

__all__ = ("GistsGistIdCommentsPostBody",)
