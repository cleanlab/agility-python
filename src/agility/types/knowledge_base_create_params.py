# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "KnowledgeBaseCreateParams",
    "IngestionPipelineParams",
    "IngestionPipelineParamsCurate",
    "IngestionPipelineParamsCurateSteps",
    "IngestionPipelineParamsCurateStepsRemoveExactDuplicatesParams",
    "IngestionPipelineParamsCurateStepsTagExactDuplicatesParams",
    "IngestionPipelineParamsCurateStepsPostpendContentParams",
    "IngestionPipelineParamsCurateDocumentStore",
    "IngestionPipelineParamsTransform",
    "IngestionPipelineParamsTransformSteps",
    "IngestionPipelineParamsTransformStepsRecursiveCharacterSplitterV0Params",
    "IngestionPipelineParamsTransformStepsNoopParams",
    "IngestionPipelineParamsVectorStore",
]


class KnowledgeBaseCreateParams(TypedDict, total=False):
    description: Required[str]

    ingestion_pipeline_params: Required[IngestionPipelineParams]
    """Knowledge base pipeline params.

    Parameters defined on the knowledge-base level for a pipeline.
    """

    name: Required[str]


class IngestionPipelineParamsCurateStepsRemoveExactDuplicatesParams(TypedDict, total=False):
    name: Literal["remove_exact_duplicates.v0"]


class IngestionPipelineParamsCurateStepsTagExactDuplicatesParams(TypedDict, total=False):
    name: Literal["tag_exact_duplicates.v0"]


class IngestionPipelineParamsCurateStepsPostpendContentParams(TypedDict, total=False):
    postpend_value: Required[str]
    """The value to postpend to the content."""

    name: Literal["postpend_content.v0"]


IngestionPipelineParamsCurateSteps: TypeAlias = Union[
    IngestionPipelineParamsCurateStepsRemoveExactDuplicatesParams,
    IngestionPipelineParamsCurateStepsTagExactDuplicatesParams,
    IngestionPipelineParamsCurateStepsPostpendContentParams,
]


class IngestionPipelineParamsCurate(TypedDict, total=False):
    steps: Dict[str, IngestionPipelineParamsCurateSteps]


class IngestionPipelineParamsCurateDocumentStore(TypedDict, total=False):
    document_tags: Dict[str, str]


class IngestionPipelineParamsTransformStepsRecursiveCharacterSplitterV0Params(TypedDict, total=False):
    chunk_overlap: int

    chunk_size: int

    name: Literal["splitters.recursive_character.v0"]


class IngestionPipelineParamsTransformStepsNoopParams(TypedDict, total=False):
    name: Literal["noop"]


IngestionPipelineParamsTransformSteps: TypeAlias = Union[
    IngestionPipelineParamsTransformStepsRecursiveCharacterSplitterV0Params,
    IngestionPipelineParamsTransformStepsNoopParams,
]


class IngestionPipelineParamsTransform(TypedDict, total=False):
    steps: Dict[str, IngestionPipelineParamsTransformSteps]


class IngestionPipelineParamsVectorStore(TypedDict, total=False):
    weaviate_collection_name: Required[str]
    """The name of the Weaviate collection to use for storing documents.

    Must start with AgilityKB and be valid.
    """

    node_tags: Dict[str, str]


class IngestionPipelineParams(TypedDict, total=False):
    curate: Required[IngestionPipelineParamsCurate]
    """Curate params.

    Defines full curation pipeline, as an ordered dict of named curation steps.
    Order of steps _does_ matter -- they are executed in the order defined.
    """

    curate_document_store: Required[IngestionPipelineParamsCurateDocumentStore]
    """Document store params."""

    transform: Required[IngestionPipelineParamsTransform]
    """Transform params.

    Defines full transform pipeline, as an ordered dict of named transform steps.
    Order of steps _does_ matter -- they are executed in the order defined.
    """

    vector_store: Required[IngestionPipelineParamsVectorStore]
    """Vector store params."""
