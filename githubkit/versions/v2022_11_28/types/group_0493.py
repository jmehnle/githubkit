"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0372 import EnterpriseWebhooksType
from .group_0373 import SimpleInstallationType
from .group_0375 import RepositoryWebhooksType
from .group_0376 import SimpleUserWebhooksType
from .group_0374 import OrganizationSimpleWebhooksType


class WebhookGollumType(TypedDict):
    """gollum event"""

    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    pages: List[WebhookGollumPropPagesItemsType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookGollumPropPagesItemsType(TypedDict):
    """WebhookGollumPropPagesItems"""

    action: Literal["created", "edited"]
    html_url: str
    page_name: str
    sha: str
    summary: Union[str, None]
    title: str


__all__ = (
    "WebhookGollumType",
    "WebhookGollumPropPagesItemsType",
)
