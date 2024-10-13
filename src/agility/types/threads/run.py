# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Run", "Usage"]


class Usage(BaseModel):
    completion_tokens: int

    prompt_tokens: int

    total_tokens: int


class Run(BaseModel):
    id: str

    assistant_id: str

    created_at: datetime

    status: Literal["pending", "in_progress", "completed", "failed", "canceled", "expired"]

    thread_id: str

    updated_at: datetime

    additional_instructions: Optional[str] = None

    deleted_at: Optional[datetime] = None

    instructions: Optional[str] = None

    knowledge_base_id: Optional[str] = None

    model: Optional[Literal["gpt-4o"]] = None

    usage: Optional[Usage] = None
