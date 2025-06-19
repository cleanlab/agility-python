# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AssistantRetrieveRunMetadataResponse"]


class AssistantRetrieveRunMetadataResponse(BaseModel):
    prompt: str

    query: str

    response: str

    context: Optional[List[str]] = None
