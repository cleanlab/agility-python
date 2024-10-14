# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SourceUpdateParams",
    "SourceParams",
    "SourceParamsWebV0Params",
    "SourceParamsNotionParams",
    "SourceSchedule",
]


class SourceUpdateParams(TypedDict, total=False):
    knowledge_base_id: Required[str]

    description: Required[str]

    name: Required[str]

    source_params: Required[SourceParams]
    """Parameters for web v0 sources."""

    source_schedule: Required[SourceSchedule]
    """Source schedule model."""


class SourceParamsWebV0Params(TypedDict, total=False):
    urls: Required[List[str]]

    allow_backward_links: bool

    allow_external_links: bool

    exclude_regex: Optional[str]

    include_regex: Optional[str]

    limit: int

    max_depth: int

    name: Literal["web_v0"]


class SourceParamsNotionParams(TypedDict, total=False):
    name: Literal["notion"]


SourceParams: TypeAlias = Union[SourceParamsWebV0Params, SourceParamsNotionParams]


class SourceSchedule(TypedDict, total=False):
    cron: Required[str]

    utc_offset: Required[int]
