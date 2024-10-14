# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["Source", "SourceParams", "SourceParamsWebV0Params", "SourceParamsNotionParams", "SourceSchedule"]


class SourceParamsWebV0Params(BaseModel):
    urls: List[str]

    allow_backward_links: Optional[bool] = None

    allow_external_links: Optional[bool] = None

    exclude_regex: Optional[str] = None

    include_regex: Optional[str] = None

    limit: Optional[int] = None

    max_depth: Optional[int] = None

    name: Optional[Literal["web_v0"]] = None


class SourceParamsNotionParams(BaseModel):
    name: Optional[Literal["notion"]] = None


SourceParams: TypeAlias = Annotated[
    Union[SourceParamsWebV0Params, SourceParamsNotionParams], PropertyInfo(discriminator="name")
]


class SourceSchedule(BaseModel):
    cron: str

    utc_offset: int


class Source(BaseModel):
    id: str

    created_at: datetime

    deleted_at: Optional[datetime] = None

    description: str

    knowledge_base_id: str

    name: str

    source_params: SourceParams
    """Parameters for web v0 sources."""

    source_schedule: SourceSchedule
    """Source schedule model."""

    status: Literal["pending", "syncing", "synced", "failed"]
    """Source status enum."""

    updated_at: datetime
