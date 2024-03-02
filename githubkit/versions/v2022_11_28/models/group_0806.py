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
from .group_0807 import WebhookWorkflowRunInProgressPropWorkflowRun


class WebhookWorkflowRunInProgress(GitHubModel):
    """workflow_run in_progress event"""

    action: Literal["in_progress"] = Field()
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
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )
    workflow: Union[WebhookWorkflowRunInProgressPropWorkflow, None] = Field(
        title="Workflow"
    )
    workflow_run: WebhookWorkflowRunInProgressPropWorkflowRun = Field()


class WebhookWorkflowRunInProgressPropWorkflow(GitHubModel):
    """Workflow"""

    badge_url: str = Field()
    created_at: datetime = Field()
    html_url: str = Field()
    id: int = Field()
    name: str = Field()
    node_id: str = Field()
    path: str = Field()
    state: str = Field()
    updated_at: datetime = Field()
    url: str = Field()


model_rebuild(WebhookWorkflowRunInProgress)
model_rebuild(WebhookWorkflowRunInProgressPropWorkflow)

__all__ = (
    "WebhookWorkflowRunInProgress",
    "WebhookWorkflowRunInProgressPropWorkflow",
)
