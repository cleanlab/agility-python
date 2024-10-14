# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Message", "Metadata"]


class Metadata(BaseModel):
    trustworthiness_score: Optional[float] = None


class Message(BaseModel):
    id: str

    content: str

    created_at: datetime

    metadata: Metadata

    role: Literal["user", "assistant"]

    thread_id: str

    updated_at: datetime

    deleted_at: Optional[datetime] = None
