# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Assistant"]


class Assistant(BaseModel):
    id: str

    created_at: datetime

    deleted_at: Optional[datetime] = None

    description: str

    name: str

    updated_at: datetime
