# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["RunSubmitToolOutputsParams", "Body"]


class RunSubmitToolOutputsParams(TypedDict, total=False):
    thread_id: Required[str]

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    output: Optional[str]

    tool_call_id: Optional[str]
