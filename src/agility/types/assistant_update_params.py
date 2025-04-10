# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["AssistantUpdateParams", "Tool", "ToolCodexV0Tool", "ToolNoOpTool"]


class AssistantUpdateParams(TypedDict, total=False):
    id: Required[str]

    description: Required[str]
    """The description of the assistant"""

    knowledge_base_id: Required[Optional[str]]

    name: Required[str]
    """The name of the assistant"""

    context_limit: Optional[int]
    """The maximum number of context chunks to include in a run."""

    instructions: Optional[str]

    logo_s3_key: Optional[str]
    """S3 object key to the assistant's logo image"""

    logo_text: Optional[str]
    """Text to display alongside the assistant's logo"""

    model: Optional[Literal["gpt-4o"]]

    suggested_questions: List[str]
    """A list of suggested questions that can be asked to the assistant"""

    tools: Optional[Iterable[Tool]]

    url_slug: Optional[str]
    """Optional URL suffix - unique identifier for the assistant's endpoint"""


class ToolCodexV0Tool(TypedDict, total=False):
    access_key: Required[str]

    type: Literal["codex_v0"]


class ToolNoOpTool(TypedDict, total=False):
    type: Literal["noop"]


Tool: TypeAlias = Union[ToolCodexV0Tool, ToolNoOpTool]
