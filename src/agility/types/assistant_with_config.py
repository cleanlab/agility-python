# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AssistantWithConfig", "Tool", "ToolFunction", "ToolFunctionParameters"]


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

    tools: Optional[List[Tool]] = None
