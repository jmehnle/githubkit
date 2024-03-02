"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0356 import EnterpriseWebhooks
from .group_0357 import SimpleInstallation
from .group_0359 import RepositoryWebhooks
from .group_0360 import SimpleUserWebhooks
from .group_0358 import OrganizationSimpleWebhooks


class WebhookSponsorshipPendingTierChange(GitHubModel):
    """sponsorship pending_tier_change event"""

    action: Literal["pending_tier_change"] = Field()
    changes: WebhookSponsorshipPendingTierChangePropChanges = Field()
    effective_date: Missing[str] = Field(
        default=UNSET,
        description="The `pending_cancellation` and `pending_tier_change` event types will include the date the cancellation or tier change will take effect.",
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    sponsorship: WebhookSponsorshipPendingTierChangePropSponsorship = Field()


class WebhookSponsorshipPendingTierChangePropSponsorship(GitHubModel):
    """WebhookSponsorshipPendingTierChangePropSponsorship"""

    created_at: str = Field()
    maintainer: Missing[
        WebhookSponsorshipPendingTierChangePropSponsorshipPropMaintainer
    ] = Field(default=UNSET)
    node_id: str = Field()
    privacy_level: str = Field()
    sponsor: Union[
        WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsor, None
    ] = Field(title="User")
    sponsorable: Union[
        WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsorable, None
    ] = Field(title="User")
    tier: WebhookSponsorshipPendingTierChangePropSponsorshipPropTier = Field(
        title="Sponsorship Tier",
        description="The `tier_changed` and `pending_tier_change` will include the original tier before the change or pending change. For more information, see the pending tier change payload.",
    )


class WebhookSponsorshipPendingTierChangePropSponsorshipPropMaintainer(GitHubModel):
    """WebhookSponsorshipPendingTierChangePropSponsorshipPropMaintainer"""

    avatar_url: Missing[str] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsor(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsorable(GitHubModel):
    """User"""

    avatar_url: Missing[str] = Field(default=UNSET)
    deleted: Missing[bool] = Field(default=UNSET)
    email: Missing[Union[str, None]] = Field(default=UNSET)
    events_url: Missing[str] = Field(default=UNSET)
    followers_url: Missing[str] = Field(default=UNSET)
    following_url: Missing[str] = Field(default=UNSET)
    gists_url: Missing[str] = Field(default=UNSET)
    gravatar_id: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: int = Field()
    login: str = Field()
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organizations_url: Missing[str] = Field(default=UNSET)
    received_events_url: Missing[str] = Field(default=UNSET)
    repos_url: Missing[str] = Field(default=UNSET)
    site_admin: Missing[bool] = Field(default=UNSET)
    starred_url: Missing[str] = Field(default=UNSET)
    subscriptions_url: Missing[str] = Field(default=UNSET)
    type: Missing[Literal["Bot", "User", "Organization"]] = Field(default=UNSET)
    url: Missing[str] = Field(default=UNSET)


class WebhookSponsorshipPendingTierChangePropSponsorshipPropTier(GitHubModel):
    """Sponsorship Tier

    The `tier_changed` and `pending_tier_change` will include the original tier
    before the change or pending change. For more information, see the pending tier
    change payload.
    """

    created_at: str = Field()
    description: str = Field()
    is_custom_ammount: Missing[bool] = Field(default=UNSET)
    is_custom_amount: Missing[bool] = Field(default=UNSET)
    is_one_time: bool = Field()
    monthly_price_in_cents: int = Field()
    monthly_price_in_dollars: int = Field()
    name: str = Field()
    node_id: str = Field()


class WebhookSponsorshipPendingTierChangePropChanges(GitHubModel):
    """WebhookSponsorshipPendingTierChangePropChanges"""

    tier: WebhookSponsorshipPendingTierChangePropChangesPropTier = Field()


class WebhookSponsorshipPendingTierChangePropChangesPropTier(GitHubModel):
    """WebhookSponsorshipPendingTierChangePropChangesPropTier"""

    from_: WebhookSponsorshipPendingTierChangePropChangesPropTierPropFrom = Field(
        alias="from",
        title="Sponsorship Tier",
        description="The `tier_changed` and `pending_tier_change` will include the original tier before the change or pending change. For more information, see the pending tier change payload.",
    )


class WebhookSponsorshipPendingTierChangePropChangesPropTierPropFrom(GitHubModel):
    """Sponsorship Tier

    The `tier_changed` and `pending_tier_change` will include the original tier
    before the change or pending change. For more information, see the pending tier
    change payload.
    """

    created_at: str = Field()
    description: str = Field()
    is_custom_ammount: Missing[bool] = Field(default=UNSET)
    is_custom_amount: Missing[bool] = Field(default=UNSET)
    is_one_time: bool = Field()
    monthly_price_in_cents: int = Field()
    monthly_price_in_dollars: int = Field()
    name: str = Field()
    node_id: str = Field()


model_rebuild(WebhookSponsorshipPendingTierChange)
model_rebuild(WebhookSponsorshipPendingTierChangePropSponsorship)
model_rebuild(WebhookSponsorshipPendingTierChangePropSponsorshipPropMaintainer)
model_rebuild(WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsor)
model_rebuild(WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsorable)
model_rebuild(WebhookSponsorshipPendingTierChangePropSponsorshipPropTier)
model_rebuild(WebhookSponsorshipPendingTierChangePropChanges)
model_rebuild(WebhookSponsorshipPendingTierChangePropChangesPropTier)
model_rebuild(WebhookSponsorshipPendingTierChangePropChangesPropTierPropFrom)

__all__ = (
    "WebhookSponsorshipPendingTierChange",
    "WebhookSponsorshipPendingTierChangePropSponsorship",
    "WebhookSponsorshipPendingTierChangePropSponsorshipPropMaintainer",
    "WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsor",
    "WebhookSponsorshipPendingTierChangePropSponsorshipPropSponsorable",
    "WebhookSponsorshipPendingTierChangePropSponsorshipPropTier",
    "WebhookSponsorshipPendingTierChangePropChanges",
    "WebhookSponsorshipPendingTierChangePropChangesPropTier",
    "WebhookSponsorshipPendingTierChangePropChangesPropTierPropFrom",
)
