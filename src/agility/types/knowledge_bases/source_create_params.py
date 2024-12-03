# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SourceCreateParams",
    "SourceParams",
    "SourceParamsWebV0Params",
    "SourceParamsWebV0ParamsScrapeOptions",
    "SourceParamsNotionV0Params",
    "SourceParamsS3PublicV0Params",
    "SourceParamsS3PrivateV0Params",
    "SourceSchedule",
]


class SourceCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    source_params: Required[SourceParams]
    """Parameters for web v0 sources."""

    source_schedule: Required[SourceSchedule]
    """Source schedule model."""

    sync: bool


class SourceParamsWebV0ParamsScrapeOptions(TypedDict, total=False):
    wait_for: int
    """
    Amount of time (in milliseconds) to wait for each page to load before scraping
    content.
    """


class SourceParamsWebV0Params(TypedDict, total=False):
    urls: Required[List[str]]

    allow_backward_links: bool

    allow_external_links: bool

    exclude_regex: Optional[str]

    include_regex: Optional[str]

    limit: int

    max_depth: int

    name: Literal["web_v0"]

    scrape_options: SourceParamsWebV0ParamsScrapeOptions
    """Parameters for scraping each crawled page."""


class SourceParamsNotionV0Params(TypedDict, total=False):
    integration_id: Required[str]

    limit: Optional[int]

    name: Literal["notion_v0"]


class SourceParamsS3PublicV0Params(TypedDict, total=False):
    bucket_name: Required[str]

    limit: Required[int]

    prefix: Required[str]

    name: Literal["s3_public_v0"]


class SourceParamsS3PrivateV0Params(TypedDict, total=False):
    bucket_name: Required[str]

    integration_id: Required[str]

    limit: Required[int]

    prefix: Required[str]

    name: Literal["s3_private_v0"]


SourceParams: TypeAlias = Union[
    SourceParamsWebV0Params, SourceParamsNotionV0Params, SourceParamsS3PublicV0Params, SourceParamsS3PrivateV0Params
]


class SourceSchedule(TypedDict, total=False):
    cron: Required[str]

    utc_offset: Required[int]
