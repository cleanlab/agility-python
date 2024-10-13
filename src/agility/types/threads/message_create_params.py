# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageCreateParams", "Metadata"]


class MessageCreateParams(TypedDict, total=False):
    content: Required[str]

    metadata: Required[Optional[Metadata]]

    role: Required[Literal["user", "assistant"]]


class Metadata(TypedDict, total=False):
    trustworthiness_score: Optional[float]
