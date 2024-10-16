# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Run", "Tool", "ToolFunction", "ToolFunctionParameters", "Usage"]


class ToolFunctionParameters(BaseModel):
    type: str

    properties: Optional[Dict[str, object]] = None

    required: Optional[List[str]] = None


class ToolFunction(BaseModel):
    description: str
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    name: str
    """The name of the function to be called."""

    parameters: Optional[ToolFunctionParameters] = None

    strict: Optional[bool] = None


class Tool(BaseModel):
    function: ToolFunction

    type: Literal["function"]


class Usage(BaseModel):
    completion_tokens: int

    prompt_tokens: int

    total_tokens: int


class Run(BaseModel):
    id: str

    assistant_id: str

    created_at: datetime

    status: Literal["pending", "in_progress", "completed", "failed", "canceled", "expired", "requires_action"]

    thread_id: str

    updated_at: datetime

    additional_instructions: Optional[str] = None

    deleted_at: Optional[datetime] = None

    instructions: Optional[str] = None

    knowledge_base_id: Optional[str] = None

    model: Optional[Literal["gpt-4o"]] = None

    tools: Optional[List[Tool]] = None

    usage: Optional[Usage] = None
