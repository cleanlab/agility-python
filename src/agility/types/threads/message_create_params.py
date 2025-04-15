# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "MessageCreateParams",
    "Metadata",
    "MetadataScores",
    "MetadataScoresContextSufficiency",
    "MetadataScoresContextSufficiencyLog",
    "MetadataScoresQueryEase",
    "MetadataScoresQueryEaseLog",
    "MetadataScoresResponseGroundedness",
    "MetadataScoresResponseGroundednessLog",
    "MetadataScoresResponseHelpfulness",
    "MetadataScoresResponseHelpfulnessLog",
    "MetadataScoresTrustworthiness",
    "MetadataScoresTrustworthinessLog",
]


class MessageCreateParams(TypedDict, total=False):
    content: Required[str]

    metadata: Required[Optional[Metadata]]

    role: Required[Literal["user", "assistant"]]


class MetadataScoresContextSufficiencyLog(TypedDict, total=False):
    explanation: Required[str]


class MetadataScoresContextSufficiency(TypedDict, total=False):
    is_bad: Optional[bool]

    log: Optional[MetadataScoresContextSufficiencyLog]

    score: Optional[float]


class MetadataScoresQueryEaseLog(TypedDict, total=False):
    explanation: Required[str]


class MetadataScoresQueryEase(TypedDict, total=False):
    is_bad: Optional[bool]

    log: Optional[MetadataScoresQueryEaseLog]

    score: Optional[float]


class MetadataScoresResponseGroundednessLog(TypedDict, total=False):
    explanation: Required[str]


class MetadataScoresResponseGroundedness(TypedDict, total=False):
    is_bad: Optional[bool]

    log: Optional[MetadataScoresResponseGroundednessLog]

    score: Optional[float]


class MetadataScoresResponseHelpfulnessLog(TypedDict, total=False):
    explanation: Required[str]


class MetadataScoresResponseHelpfulness(TypedDict, total=False):
    is_bad: Optional[bool]

    log: Optional[MetadataScoresResponseHelpfulnessLog]

    score: Optional[float]


class MetadataScoresTrustworthinessLog(TypedDict, total=False):
    explanation: Required[str]


class MetadataScoresTrustworthiness(TypedDict, total=False):
    is_bad: Optional[bool]

    log: Optional[MetadataScoresTrustworthinessLog]

    score: Optional[float]


class MetadataScores(TypedDict, total=False):
    context_sufficiency: Optional[MetadataScoresContextSufficiency]

    query_ease: Optional[MetadataScoresQueryEase]

    response_groundedness: Optional[MetadataScoresResponseGroundedness]

    response_helpfulness: Optional[MetadataScoresResponseHelpfulness]

    trustworthiness: Optional[MetadataScoresTrustworthiness]


class Metadata(TypedDict, total=False):
    citations: Optional[List[str]]

    is_bad_response: Optional[bool]

    is_expert_answer: Optional[bool]

    scores: Optional[MetadataScores]

    trustworthiness_explanation: Optional[str]

    trustworthiness_score: Optional[float]
