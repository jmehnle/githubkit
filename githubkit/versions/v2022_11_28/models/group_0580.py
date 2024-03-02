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


class WebhookMetaDeleted(GitHubModel):
    """meta deleted event"""

    action: Literal["deleted"] = Field()
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    hook: WebhookMetaDeletedPropHook = Field(
        description="The modified webhook. This will contain different keys based on the type of webhook it is: repository, organization, business, app, or GitHub Marketplace."
    )
    hook_id: int = Field(description="The id of the modified webhook.")
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
    repository: Missing[Union[None, RepositoryWebhooks]] = Field(default=UNSET)
    sender: Missing[SimpleUserWebhooks] = Field(
        default=UNSET,
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookMetaDeletedPropHook(GitHubModel):
    """WebhookMetaDeletedPropHook

    The modified webhook. This will contain different keys based on the type of
    webhook it is: repository, organization, business, app, or GitHub Marketplace.
    """

    active: bool = Field()
    config: WebhookMetaDeletedPropHookPropConfig = Field()
    created_at: str = Field()
    events: List[
        Literal[
            "*",
            "branch_protection_rule",
            "check_run",
            "check_suite",
            "code_scanning_alert",
            "commit_comment",
            "create",
            "delete",
            "deployment",
            "deployment_status",
            "deploy_key",
            "discussion",
            "discussion_comment",
            "fork",
            "gollum",
            "issues",
            "issue_comment",
            "label",
            "member",
            "membership",
            "meta",
            "milestone",
            "organization",
            "org_block",
            "package",
            "page_build",
            "project",
            "project_card",
            "project_column",
            "public",
            "pull_request",
            "pull_request_review",
            "pull_request_review_comment",
            "pull_request_review_thread",
            "push",
            "registry_package",
            "release",
            "repository",
            "repository_import",
            "repository_vulnerability_alert",
            "secret_scanning_alert",
            "secret_scanning_alert_location",
            "security_and_analysis",
            "star",
            "status",
            "team",
            "team_add",
            "watch",
            "workflow_job",
            "workflow_run",
            "repository_dispatch",
            "projects_v2_item",
        ]
    ] = Field()
    id: int = Field()
    name: str = Field()
    type: str = Field()
    updated_at: str = Field()


class WebhookMetaDeletedPropHookPropConfig(GitHubModel):
    """WebhookMetaDeletedPropHookPropConfig"""

    content_type: Literal["json", "form"] = Field()
    insecure_ssl: str = Field()
    secret: Missing[str] = Field(default=UNSET)
    url: str = Field()


model_rebuild(WebhookMetaDeleted)
model_rebuild(WebhookMetaDeletedPropHook)
model_rebuild(WebhookMetaDeletedPropHookPropConfig)

__all__ = (
    "WebhookMetaDeleted",
    "WebhookMetaDeletedPropHook",
    "WebhookMetaDeletedPropHookPropConfig",
)
