# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AssistantUpdateParams"]


class AssistantUpdateParams(TypedDict, total=False):
    id: Required[str]

    description: Required[str]

    knowledge_base_id: Required[str]

    name: Required[str]

    instructions: Optional[str]

    model: Optional[Literal["gpt-4o"]]
