"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0167 import DeploymentType
from .group_0288 import PullRequestType
from .group_0357 import SimpleInstallationType
from .group_0359 import RepositoryWebhooksType
from .group_0360 import SimpleUserWebhooksType
from .group_0358 import OrganizationSimpleWebhooksType


class WebhookDeploymentProtectionRuleRequestedType(TypedDict):
    """deployment protection rule requested event"""

    action: Literal["requested"]
    environment: NotRequired[str]
    event: NotRequired[str]
    deployment_callback_url: NotRequired[str]
    deployment: NotRequired[DeploymentType]
    pull_requests: NotRequired[List[PullRequestType]]
    repository: NotRequired[RepositoryWebhooksType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    sender: NotRequired[SimpleUserWebhooksType]


__all__ = ("WebhookDeploymentProtectionRuleRequestedType",)
