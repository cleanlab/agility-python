# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["S3V0Integration", "ResourceAccessDefinition", "ResourceAccessDefinitionResource"]


class ResourceAccessDefinitionResource(BaseModel):
    bucket_name: str

    prefix: str

    resource_type: Optional[Literal["s3/v0"]] = None


class ResourceAccessDefinition(BaseModel):
    policy: object

    resource: ResourceAccessDefinitionResource


class S3V0Integration(BaseModel):
    id: str

    principal_id: str

    resource_access_definition: ResourceAccessDefinition

    state: Literal["ready", "pending", "error"]

    integration_category: Optional[Literal["rbac"]] = None

    integration_type: Optional[Literal["s3/v0", "gcs/v0"]] = None
