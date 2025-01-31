"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired

from .group_0371 import MetaType
from .group_0381 import ScimEnterpriseUserResponseAllof1PropGroupsItemsType


class ScimEnterpriseUserResponseAllof1Type(TypedDict):
    """ScimEnterpriseUserResponseAllof1"""

    id: str
    groups: NotRequired[List[ScimEnterpriseUserResponseAllof1PropGroupsItemsType]]
    meta: MetaType


__all__ = ("ScimEnterpriseUserResponseAllof1Type",)
