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


class WebhookCodeScanningAlertAppearedInBranch(GitHubModel):
    """code_scanning_alert appeared_in_branch event"""

    action: Literal["appeared_in_branch"] = Field()
    alert: WebhookCodeScanningAlertAppearedInBranchPropAlert = Field(
        description="The code scanning alert involved in the event."
    )
    commit_oid: str = Field(
        description="The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty."
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
    ref: str = Field(
        description="The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty."
    )
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookCodeScanningAlertAppearedInBranchPropAlert(GitHubModel):
    """WebhookCodeScanningAlertAppearedInBranchPropAlert

    The code scanning alert involved in the event.
    """

    created_at: datetime = Field(
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`"
    )
    dismissed_at: Union[datetime, None] = Field(
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."
    )
    dismissed_by: Union[
        WebhookCodeScanningAlertAppearedInBranchPropAlertPropDismissedBy, None
    ] = Field(title="User")
    dismissed_reason: Union[
        None, Literal["false positive", "won't fix", "used in tests"]
    ] = Field(description="The reason for dismissing or closing the alert.")
    html_url: str = Field(description="The GitHub URL of the alert resource.")
    most_recent_instance: Missing[
        Union[
            WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstance,
            None,
        ]
    ] = Field(default=UNSET, title="Alert Instance")
    number: int = Field(description="The code scanning alert number.")
    rule: WebhookCodeScanningAlertAppearedInBranchPropAlertPropRule = Field()
    state: Literal["open", "dismissed", "fixed"] = Field(
        description="State of a code scanning alert."
    )
    tool: WebhookCodeScanningAlertAppearedInBranchPropAlertPropTool = Field()
    url: str = Field()


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropDismissedBy(GitHubModel):
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


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstance(
    GitHubModel
):
    """Alert Instance"""

    analysis_key: str = Field(
        description="Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name."
    )
    category: Missing[str] = Field(
        default=UNSET,
        description="Identifies the configuration under which the analysis was executed.",
    )
    classifications: Missing[List[str]] = Field(default=UNSET)
    commit_sha: Missing[str] = Field(default=UNSET)
    environment: str = Field(
        description="Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed."
    )
    location: Missing[
        WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropLocation
    ] = Field(default=UNSET)
    message: Missing[
        WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropMessage
    ] = Field(default=UNSET)
    ref: str = Field(
        description="The full Git reference, formatted as `refs/heads/<branch name>`."
    )
    state: Literal["open", "dismissed", "fixed"] = Field(
        description="State of a code scanning alert."
    )


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropLocation(
    GitHubModel
):
    """WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropLocat
    ion
    """

    end_column: Missing[int] = Field(default=UNSET)
    end_line: Missing[int] = Field(default=UNSET)
    path: Missing[str] = Field(default=UNSET)
    start_column: Missing[int] = Field(default=UNSET)
    start_line: Missing[int] = Field(default=UNSET)


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropMessage(
    GitHubModel
):
    """WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropMessa
    ge
    """

    text: Missing[str] = Field(default=UNSET)


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropRule(GitHubModel):
    """WebhookCodeScanningAlertAppearedInBranchPropAlertPropRule"""

    description: str = Field(
        description="A short description of the rule used to detect the alert."
    )
    id: str = Field(
        description="A unique identifier for the rule used to detect the alert."
    )
    severity: Union[None, Literal["none", "note", "warning", "error"]] = Field(
        description="The severity of the alert."
    )


class WebhookCodeScanningAlertAppearedInBranchPropAlertPropTool(GitHubModel):
    """WebhookCodeScanningAlertAppearedInBranchPropAlertPropTool"""

    name: str = Field(
        description="The name of the tool used to generate the code scanning analysis alert."
    )
    version: Union[str, None] = Field(
        description="The version of the tool used to detect the alert."
    )


model_rebuild(WebhookCodeScanningAlertAppearedInBranch)
model_rebuild(WebhookCodeScanningAlertAppearedInBranchPropAlert)
model_rebuild(WebhookCodeScanningAlertAppearedInBranchPropAlertPropDismissedBy)
model_rebuild(WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstance)
model_rebuild(
    WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropLocation
)
model_rebuild(
    WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropMessage
)
model_rebuild(WebhookCodeScanningAlertAppearedInBranchPropAlertPropRule)
model_rebuild(WebhookCodeScanningAlertAppearedInBranchPropAlertPropTool)

__all__ = (
    "WebhookCodeScanningAlertAppearedInBranch",
    "WebhookCodeScanningAlertAppearedInBranchPropAlert",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropDismissedBy",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstance",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropLocation",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropMostRecentInstancePropMessage",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropRule",
    "WebhookCodeScanningAlertAppearedInBranchPropAlertPropTool",
)
