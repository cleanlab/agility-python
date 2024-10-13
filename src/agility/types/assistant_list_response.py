# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .assistant_with_config import AssistantWithConfig

__all__ = ["AssistantListResponse"]

AssistantListResponse: TypeAlias = List[AssistantWithConfig]
