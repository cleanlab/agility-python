# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AssistantCreateParams"]


class AssistantCreateParams(TypedDict, total=False):
    description: Required[str]
    """The description of the assistant"""

    knowledge_base_id: Required[str]

    name: Required[str]
    """The name of the assistant"""

    instructions: Optional[str]

    model: Optional[Literal["gpt-4o"]]

    suggested_questions: List[str]
    """A list of suggested questions that can be asked to the assistant"""

    url_slug: Optional[str]
    """Optional URL suffix - unique identifier for the assistant's endpoint"""
