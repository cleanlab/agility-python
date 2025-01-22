# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["Run", "Tool", "ToolCodexV0Tool", "ToolNoOpTool", "Usage"]


class ToolCodexV0Tool(BaseModel):
    access_key: str

    type: Optional[Literal["codex_v0"]] = None


class ToolNoOpTool(BaseModel):
    type: Optional[Literal["noop"]] = None


Tool: TypeAlias = Union[ToolCodexV0Tool, ToolNoOpTool]


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

    context_limit: Optional[int] = None
    """The maximum number of context chunks to include."""

    deleted_at: Optional[datetime] = None

    instructions: Optional[str] = None

    knowledge_base_id: Optional[str] = None

    last_error: Optional[str] = None

    model: Optional[Literal["gpt-4o"]] = None

    tools: Optional[List[Tool]] = None

    usage: Optional[Usage] = None
