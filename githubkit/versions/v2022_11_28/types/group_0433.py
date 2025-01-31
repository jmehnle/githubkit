"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired

from .group_0373 import SimpleInstallationType
from .group_0375 import RepositoryWebhooksType
from .group_0376 import SimpleUserWebhooksType
from .group_0374 import OrganizationSimpleWebhooksType
from .group_0379 import CheckRunWithSimpleCheckSuiteType


class WebhookCheckRunRequestedActionType(TypedDict):
    """Check Run Requested Action Event"""

    action: Literal["requested_action"]
    check_run: CheckRunWithSimpleCheckSuiteType
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    requested_action: NotRequired[WebhookCheckRunRequestedActionPropRequestedActionType]
    sender: SimpleUserWebhooksType


class WebhookCheckRunRequestedActionPropRequestedActionType(TypedDict):
    """WebhookCheckRunRequestedActionPropRequestedAction

    The action requested by the user.
    """

    identifier: NotRequired[str]


__all__ = (
    "WebhookCheckRunRequestedActionType",
    "WebhookCheckRunRequestedActionPropRequestedActionType",
)
