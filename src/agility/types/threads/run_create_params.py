# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "RunCreateParams",
    "AdditionalMessage",
    "AdditionalMessageMetadata",
    "Tool",
    "ToolFunction",
    "ToolFunctionParameters",
]


class RunCreateParams(TypedDict, total=False):
    assistant_id: Required[str]

    additional_instructions: Optional[str]

    additional_messages: Iterable[AdditionalMessage]

    instructions: Optional[str]

    knowledge_base_id: Optional[str]

    model: Optional[Literal["gpt-4o"]]

    tools: Optional[Iterable[Tool]]


class AdditionalMessageMetadata(TypedDict, total=False):
    trustworthiness_score: Optional[float]


class AdditionalMessage(TypedDict, total=False):
    content: Required[str]

    metadata: Required[AdditionalMessageMetadata]

    role: Required[Literal["user", "assistant"]]

    thread_id: Required[str]


class ToolFunctionParameters(TypedDict, total=False):
    type: Required[str]

    additional_properties: Annotated[bool, PropertyInfo(alias="additionalProperties")]

    properties: Dict[str, object]

    required: Optional[List[str]]


class ToolFunction(TypedDict, total=False):
    description: Required[str]
    """
    A description of what the function does, used by the model to choose when and
    how to call the function.
    """

    name: Required[str]
    """The name of the function to be called."""

    parameters: Optional[ToolFunctionParameters]

    strict: bool


class Tool(TypedDict, total=False):
    function: Required[ToolFunction]

    type: Required[Literal["function"]]
