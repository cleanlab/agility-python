# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "RunCreateParams",
    "AdditionalMessage",
    "AdditionalMessageMetadata",
    "Tool",
    "ToolAlphaV0Tool",
    "ToolNoOpTool",
]


class RunCreateParams(TypedDict, total=False):
    assistant_id: Required[str]

    additional_instructions: Optional[str]

    additional_messages: Iterable[AdditionalMessage]

    context_limit: Optional[int]
    """The maximum number of context chunks to include."""

    instructions: Optional[str]

    knowledge_base_id: Optional[str]

    model: Optional[Literal["gpt-4o"]]

    tools: Optional[Iterable[Tool]]


class AdditionalMessageMetadata(TypedDict, total=False):
    citations: Optional[List[str]]

    trustworthiness_score: Optional[float]


class AdditionalMessage(TypedDict, total=False):
    content: Required[str]

    metadata: Required[AdditionalMessageMetadata]

    role: Required[Literal["user", "assistant"]]

    thread_id: Required[str]


class ToolAlphaV0Tool(TypedDict, total=False):
    access_key: Required[str]

    project_id: Required[int]

    name: Literal["alpha_v0"]


class ToolNoOpTool(TypedDict, total=False):
    name: Literal["noop"]


Tool: TypeAlias = Union[ToolAlphaV0Tool, ToolNoOpTool]
