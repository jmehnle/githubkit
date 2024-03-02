"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class UserCodespacesPostBodyOneof0Type(TypedDict):
    """UserCodespacesPostBodyOneof0"""

    repository_id: int
    ref: NotRequired[str]
    location: NotRequired[str]
    geo: NotRequired[Literal["EuropeWest", "SoutheastAsia", "UsEast", "UsWest"]]
    client_ip: NotRequired[str]
    machine: NotRequired[str]
    devcontainer_path: NotRequired[str]
    multi_repo_permissions_opt_out: NotRequired[bool]
    working_directory: NotRequired[str]
    idle_timeout_minutes: NotRequired[int]
    display_name: NotRequired[str]
    retention_period_minutes: NotRequired[int]


__all__ = ("UserCodespacesPostBodyOneof0Type",)
