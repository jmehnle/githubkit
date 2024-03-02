"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0366 import ProjectsV2Type
from .group_0357 import SimpleInstallationType
from .group_0360 import SimpleUserWebhooksType
from .group_0358 import OrganizationSimpleWebhooksType


class WebhookProjectsV2ProjectClosedType(TypedDict):
    """Projects v2 Project Closed Event"""

    action: Literal["closed"]
    installation: NotRequired[SimpleInstallationType]
    organization: OrganizationSimpleWebhooksType
    projects_v2: ProjectsV2Type
    sender: SimpleUserWebhooksType


__all__ = ("WebhookProjectsV2ProjectClosedType",)
