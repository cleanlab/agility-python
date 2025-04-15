# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "Message",
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


class MetadataScoresContextSufficiencyLog(BaseModel):
    explanation: Optional[str] = None


class MetadataScoresContextSufficiency(BaseModel):
    is_bad: Optional[bool] = None

    log: Optional[MetadataScoresContextSufficiencyLog] = None

    score: Optional[float] = None


class MetadataScoresQueryEaseLog(BaseModel):
    explanation: Optional[str] = None


class MetadataScoresQueryEase(BaseModel):
    is_bad: Optional[bool] = None

    log: Optional[MetadataScoresQueryEaseLog] = None

    score: Optional[float] = None


class MetadataScoresResponseGroundednessLog(BaseModel):
    explanation: Optional[str] = None


class MetadataScoresResponseGroundedness(BaseModel):
    is_bad: Optional[bool] = None

    log: Optional[MetadataScoresResponseGroundednessLog] = None

    score: Optional[float] = None


class MetadataScoresResponseHelpfulnessLog(BaseModel):
    explanation: Optional[str] = None


class MetadataScoresResponseHelpfulness(BaseModel):
    is_bad: Optional[bool] = None

    log: Optional[MetadataScoresResponseHelpfulnessLog] = None

    score: Optional[float] = None


class MetadataScoresTrustworthinessLog(BaseModel):
    explanation: Optional[str] = None


class MetadataScoresTrustworthiness(BaseModel):
    is_bad: Optional[bool] = None

    log: Optional[MetadataScoresTrustworthinessLog] = None

    score: Optional[float] = None


class MetadataScores(BaseModel):
    context_sufficiency: Optional[MetadataScoresContextSufficiency] = None

    query_ease: Optional[MetadataScoresQueryEase] = None

    response_groundedness: Optional[MetadataScoresResponseGroundedness] = None

    response_helpfulness: Optional[MetadataScoresResponseHelpfulness] = None

    trustworthiness: Optional[MetadataScoresTrustworthiness] = None


class Metadata(BaseModel):
    citations: Optional[List[str]] = None

    is_bad_response: Optional[bool] = None

    is_expert_answer: Optional[bool] = None

    scores: Optional[MetadataScores] = None

    trustworthiness_explanation: Optional[str] = None

    trustworthiness_score: Optional[float] = None


class Message(BaseModel):
    id: str

    content: str

    created_at: datetime

    metadata: Metadata

    role: Literal["user", "assistant"]

    thread_id: str

    updated_at: datetime

    deleted_at: Optional[datetime] = None
