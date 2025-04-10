# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["AssistantListResponse", "Tool", "ToolCodexV0Tool", "ToolNoOpTool"]


class ToolCodexV0Tool(BaseModel):
    access_key: str

    type: Optional[Literal["codex_v0"]] = None


class ToolNoOpTool(BaseModel):
    type: Optional[Literal["noop"]] = None


Tool: TypeAlias = Union[ToolCodexV0Tool, ToolNoOpTool]


class AssistantListResponse(BaseModel):
    id: str

    created_at: datetime

    deleted_at: Optional[datetime] = None

    description: str
    """The description of the assistant"""

    knowledge_base_id: Optional[str] = None

    knowledge_base_name: Optional[str] = None

    name: str
    """The name of the assistant"""

    updated_at: datetime

    context_limit: Optional[int] = None
    """The maximum number of context chunks to include in a run."""

    instructions: Optional[str] = None

    logo_s3_key: Optional[str] = None
    """S3 object key to the assistant's logo image"""

    logo_text: Optional[str] = None
    """Text to display alongside the assistant's logo"""

    model: Optional[Literal["gpt-4o"]] = None

    suggested_questions: Optional[List[str]] = None
    """A list of suggested questions that can be asked to the assistant"""

    tools: Optional[List[Tool]] = None

    url_slug: Optional[str] = None
    """Optional URL suffix - unique identifier for the assistant's endpoint"""
