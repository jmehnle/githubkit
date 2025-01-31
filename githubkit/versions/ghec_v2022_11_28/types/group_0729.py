"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0406 import EnterpriseWebhooksType
from .group_0407 import SimpleInstallationType
from .group_0409 import RepositoryWebhooksType
from .group_0410 import SimpleUserWebhooksType
from .group_0408 import OrganizationSimpleWebhooksType


class WebhookRepositoryEditedType(TypedDict):
    """repository edited event"""

    action: Literal["edited"]
    changes: WebhookRepositoryEditedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookRepositoryEditedPropChangesType(TypedDict):
    """WebhookRepositoryEditedPropChanges"""

    default_branch: NotRequired[WebhookRepositoryEditedPropChangesPropDefaultBranchType]
    description: NotRequired[WebhookRepositoryEditedPropChangesPropDescriptionType]
    homepage: NotRequired[WebhookRepositoryEditedPropChangesPropHomepageType]
    topics: NotRequired[WebhookRepositoryEditedPropChangesPropTopicsType]


class WebhookRepositoryEditedPropChangesPropDefaultBranchType(TypedDict):
    """WebhookRepositoryEditedPropChangesPropDefaultBranch"""

    from_: str


class WebhookRepositoryEditedPropChangesPropDescriptionType(TypedDict):
    """WebhookRepositoryEditedPropChangesPropDescription"""

    from_: Union[str, None]


class WebhookRepositoryEditedPropChangesPropHomepageType(TypedDict):
    """WebhookRepositoryEditedPropChangesPropHomepage"""

    from_: Union[str, None]


class WebhookRepositoryEditedPropChangesPropTopicsType(TypedDict):
    """WebhookRepositoryEditedPropChangesPropTopics"""

    from_: NotRequired[Union[List[str], None]]


__all__ = (
    "WebhookRepositoryEditedType",
    "WebhookRepositoryEditedPropChangesType",
    "WebhookRepositoryEditedPropChangesPropDefaultBranchType",
    "WebhookRepositoryEditedPropChangesPropDescriptionType",
    "WebhookRepositoryEditedPropChangesPropHomepageType",
    "WebhookRepositoryEditedPropChangesPropTopicsType",
)
