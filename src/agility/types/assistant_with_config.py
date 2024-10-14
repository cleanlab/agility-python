# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AssistantWithConfig"]


class AssistantWithConfig(BaseModel):
    id: str

    created_at: datetime

    deleted_at: Optional[datetime] = None

    description: str

    knowledge_base_id: str

    name: str

    updated_at: datetime

    instructions: Optional[str] = None

    model: Optional[Literal["gpt-4o"]] = None
