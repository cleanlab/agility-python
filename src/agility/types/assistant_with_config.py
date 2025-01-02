# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["AssistantWithConfig", "Tool", "ToolAlphaV0Tool", "ToolNoOpTool"]


class ToolAlphaV0Tool(BaseModel):
    access_key: str

    project_id: int

    name: Optional[Literal["alpha_v0"]] = None


class ToolNoOpTool(BaseModel):
    name: Optional[Literal["noop"]] = None


Tool: TypeAlias = Union[ToolAlphaV0Tool, ToolNoOpTool]


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

    tools: Optional[List[Tool]] = None

    url_slug: Optional[str] = None
    """Optional URL suffix - unique identifier for the assistant's endpoint"""
