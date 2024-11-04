# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .s3_v0_integration import S3V0Integration
from .gc_sv0_integration import GcSv0Integration

__all__ = ["IntegrationCreateResponse"]

IntegrationCreateResponse: TypeAlias = Union[S3V0Integration, GcSv0Integration]
