# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageCreateParams", "Metadata", "MetadataScores"]


class MessageCreateParams(TypedDict, total=False):
    content: Required[str]

    metadata: Required[Optional[Metadata]]

    role: Required[Literal["user", "assistant"]]


class MetadataScores(TypedDict, total=False):
    response_helpfulness: Optional[Dict[str, object]]

    trustworthiness: Optional[Dict[str, object]]


class Metadata(TypedDict, total=False):
    citations: Optional[List[str]]

    is_bad_response: Optional[bool]

    is_expert_answer: Optional[bool]

    scores: Optional[MetadataScores]

    trustworthiness_explanation: Optional[str]

    trustworthiness_score: Optional[float]
