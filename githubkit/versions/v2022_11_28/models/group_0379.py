"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class WebhookCheckRunRequestedActionFormEncoded(GitHubModel):
    """Check Run Requested Action Event

    The check_run.requested_action webhook encoded with URL encoding
    """

    payload: str = Field(
        description="A URL-encoded string of the check_run.requested_action JSON payload. The decoded payload is a JSON object."
    )


model_rebuild(WebhookCheckRunRequestedActionFormEncoded)

__all__ = ("WebhookCheckRunRequestedActionFormEncoded",)
