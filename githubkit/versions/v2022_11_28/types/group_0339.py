"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypedDict, NotRequired

from .group_0334 import SearchResultTextMatchesItemsType


class LabelSearchResultItemType(TypedDict):
    """Label Search Result Item

    Label Search Result Item
    """

    id: int
    node_id: str
    url: str
    name: str
    color: str
    default: bool
    description: Union[str, None]
    score: float
    text_matches: NotRequired[List[SearchResultTextMatchesItemsType]]


class SearchLabelsGetResponse200Type(TypedDict):
    """SearchLabelsGetResponse200"""

    total_count: int
    incomplete_results: bool
    items: List[LabelSearchResultItemType]


__all__ = (
    "LabelSearchResultItemType",
    "SearchLabelsGetResponse200Type",
)
