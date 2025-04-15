# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["AssistantCreateParams", "ResponseValidationConfig", "Tool", "ToolCodexV0Tool", "ToolNoOpTool"]


class AssistantCreateParams(TypedDict, total=False):
    description: Required[str]
    """The description of the assistant"""

    knowledge_base_id: Required[Optional[str]]

    name: Required[str]
    """The name of the assistant"""

    codex_access_key: Optional[str]

    context_limit: Optional[int]
    """The maximum number of context chunks to include in a run."""

    instructions: Optional[str]

    logo_s3_key: Optional[str]
    """S3 object key to the assistant's logo image"""

    logo_text: Optional[str]
    """Text to display alongside the assistant's logo"""

    model: Optional[Literal["gpt-4o"]]

    response_validation_config: Optional[Iterable[ResponseValidationConfig]]

    suggested_questions: List[str]
    """A list of suggested questions that can be asked to the assistant"""

    tools: Optional[Iterable[Tool]]

    url_slug: Optional[str]
    """Optional URL suffix - unique identifier for the assistant's endpoint"""


class ResponseValidationConfig(TypedDict, total=False):
    is_bad_threshold: Required[float]

    name: Required[
        Literal["trustworthiness", "response_helpfulness", "context_sufficiency", "response_groundedness", "query_ease"]
    ]


class ToolCodexV0Tool(TypedDict, total=False):
    access_key: Required[str]

    type: Literal["codex_v0"]


class ToolNoOpTool(TypedDict, total=False):
    type: Literal["noop"]


Tool: TypeAlias = Union[ToolCodexV0Tool, ToolNoOpTool]
