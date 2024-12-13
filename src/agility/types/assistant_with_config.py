# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AssistantWithConfig"]


class AssistantWithConfig(BaseModel):
    id: str

    created_at: datetime

    deleted_at: Optional[datetime] = None

    description: str
    """The description of the assistant"""

    knowledge_base_id: Optional[str] = None

    name: str
    """The name of the assistant"""

    updated_at: datetime

    context_limit: Optional[int] = None
    """The maximum number of context chunks to include in a run."""

    instructions: Optional[str] = None

    model: Optional[Literal["gpt-4o"]] = None

    suggested_questions: Optional[List[str]] = None
    """A list of suggested questions that can be asked to the assistant"""

    url_slug: Optional[str] = None
    """Optional URL suffix - unique identifier for the assistant's endpoint"""
