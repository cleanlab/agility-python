# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RunCreateParams", "AdditionalMessage", "AdditionalMessageMetadata"]


class RunCreateParams(TypedDict, total=False):
    assistant_id: Required[str]

    additional_instructions: Optional[str]

    additional_messages: Iterable[AdditionalMessage]

    instructions: Optional[str]

    knowledge_base_id: Optional[str]

    model: Optional[Literal["gpt-4o"]]


class AdditionalMessageMetadata(TypedDict, total=False):
    trustworthiness_score: Optional[float]


class AdditionalMessage(TypedDict, total=False):
    content: Required[str]

    metadata: Required[AdditionalMessageMetadata]

    role: Required[Literal["user", "assistant"]]

    thread_id: Required[str]
