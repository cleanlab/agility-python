# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Message", "Metadata", "MetadataScores"]


class MetadataScores(BaseModel):
    response_helpfulness: Optional[Dict[str, object]] = None

    trustworthiness: Optional[Dict[str, object]] = None


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
