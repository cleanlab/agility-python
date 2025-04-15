# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "RunStreamParams",
    "AdditionalMessage",
    "AdditionalMessageMetadata",
    "AdditionalMessageMetadataScores",
    "AdditionalMessageMetadataScoresContextSufficiency",
    "AdditionalMessageMetadataScoresContextSufficiencyLog",
    "AdditionalMessageMetadataScoresQueryEase",
    "AdditionalMessageMetadataScoresQueryEaseLog",
    "AdditionalMessageMetadataScoresResponseGroundedness",
    "AdditionalMessageMetadataScoresResponseGroundednessLog",
    "AdditionalMessageMetadataScoresResponseHelpfulness",
    "AdditionalMessageMetadataScoresResponseHelpfulnessLog",
    "AdditionalMessageMetadataScoresTrustworthiness",
    "AdditionalMessageMetadataScoresTrustworthinessLog",
    "ResponseValidationConfig",
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

    response_validation_config: Optional[Iterable[ResponseValidationConfig]]

    tools: Optional[Iterable[Tool]]


class AdditionalMessageMetadataScoresContextSufficiencyLog(TypedDict, total=False):
    explanation: Optional[str]


class AdditionalMessageMetadataScoresContextSufficiency(TypedDict, total=False):
    is_bad: Optional[bool]

    log: Optional[AdditionalMessageMetadataScoresContextSufficiencyLog]

    score: Optional[float]


class AdditionalMessageMetadataScoresQueryEaseLog(TypedDict, total=False):
    explanation: Optional[str]


class AdditionalMessageMetadataScoresQueryEase(TypedDict, total=False):
    is_bad: Optional[bool]

    log: Optional[AdditionalMessageMetadataScoresQueryEaseLog]

    score: Optional[float]


class AdditionalMessageMetadataScoresResponseGroundednessLog(TypedDict, total=False):
    explanation: Optional[str]


class AdditionalMessageMetadataScoresResponseGroundedness(TypedDict, total=False):
    is_bad: Optional[bool]

    log: Optional[AdditionalMessageMetadataScoresResponseGroundednessLog]

    score: Optional[float]


class AdditionalMessageMetadataScoresResponseHelpfulnessLog(TypedDict, total=False):
    explanation: Optional[str]


class AdditionalMessageMetadataScoresResponseHelpfulness(TypedDict, total=False):
    is_bad: Optional[bool]

    log: Optional[AdditionalMessageMetadataScoresResponseHelpfulnessLog]

    score: Optional[float]


class AdditionalMessageMetadataScoresTrustworthinessLog(TypedDict, total=False):
    explanation: Optional[str]


class AdditionalMessageMetadataScoresTrustworthiness(TypedDict, total=False):
    is_bad: Optional[bool]

    log: Optional[AdditionalMessageMetadataScoresTrustworthinessLog]

    score: Optional[float]


class AdditionalMessageMetadataScores(TypedDict, total=False):
    context_sufficiency: Optional[AdditionalMessageMetadataScoresContextSufficiency]

    query_ease: Optional[AdditionalMessageMetadataScoresQueryEase]

    response_groundedness: Optional[AdditionalMessageMetadataScoresResponseGroundedness]

    response_helpfulness: Optional[AdditionalMessageMetadataScoresResponseHelpfulness]

    trustworthiness: Optional[AdditionalMessageMetadataScoresTrustworthiness]


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
