# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IntegrationTypeDef"]


class IntegrationTypeDef(BaseModel):
    description: str

    integration_category: Literal["rbac"]

    integration_type: Literal["s3/v0", "gcs/v0"]

    name: str
