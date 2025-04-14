# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "RunStreamParams",
    "AdditionalMessage",
    "AdditionalMessageMetadata",
    "AdditionalMessageMetadataScores",
    "Tool",
    "ToolCodexV0Tool",
    "ToolNoOpTool",
]


class RunStreamParams(TypedDict, total=False):
    assistant_id: Required[str]

    additional_instructions: Optional[str]

    additional_messages: Iterable[AdditionalMessage]

    codex_access_key: Optional[str]

    context_limit: Optional[int]
    """The maximum number of context chunks to include."""

    instructions: Optional[str]

    knowledge_base_id: Optional[str]

    model: Optional[Literal["gpt-4o"]]

    tools: Optional[Iterable[Tool]]


class AdditionalMessageMetadataScores(TypedDict, total=False):
    response_helpfulness: Optional[Dict[str, object]]

    trustworthiness: Optional[Dict[str, object]]


class AdditionalMessageMetadata(TypedDict, total=False):
    citations: Optional[List[str]]

    is_bad_response: Optional[bool]

    is_expert_answer: Optional[bool]

    scores: Optional[AdditionalMessageMetadataScores]

    trustworthiness_explanation: Optional[str]

    trustworthiness_score: Optional[float]


class AdditionalMessage(TypedDict, total=False):
    content: Required[str]

    metadata: Required[AdditionalMessageMetadata]

    role: Required[Literal["user", "assistant"]]

    thread_id: Required[str]


class ToolCodexV0Tool(TypedDict, total=False):
    access_key: Required[str]

    type: Literal["codex_v0"]


class ToolNoOpTool(TypedDict, total=False):
    type: Literal["noop"]


Tool: TypeAlias = Union[ToolCodexV0Tool, ToolNoOpTool]
