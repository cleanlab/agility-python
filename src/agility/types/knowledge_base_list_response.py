# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .knowledge_base_with_config import KnowledgeBaseWithConfig

__all__ = ["KnowledgeBaseListResponse"]

KnowledgeBaseListResponse: TypeAlias = List[KnowledgeBaseWithConfig]
