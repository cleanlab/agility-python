# Agility Python API library

# Installation

You can install the Agility python client from [our internal repo](https://github.com/cleanlab/agility-python) with:

```python
pip install git+ssh://git@github.com/cleanlab/agility-python.git
```

# Overview

This user guide goes over the basic concepts of Agility and includes an example of how to create an Agility assistant.

Cleanlab Agility is an end-to-end API that allows you to create trustworthy AI applications. The API allows you to build reliable RAG systems by ingesting data from a wide variety of sources into Knowledge Bases and by creating AI Assistants that can respond to user queries while accessing the relevant data and providing reliable, interpretable answers. 

## Concepts

### Knowledge Bases

- **Knowledge Bases** -
- **Sources** -
- **Documents** -

### Assistants

- **Assistant**  - An AI Assistant that will respond to user queries, while referencing user-supplied data sources and instructions.
- **Threads -** A conversation session between a user and Assistant. Threads store Messages and retrieve context from Knowledge Bases to provide trustworthy results
- **Messages -** A message created by a user or Assistant. Messages are represented as text and are attached to a parent Thread
- **Runs -** Invokes the Assistant for a specific Thread. It uses the configuration for the Assistant as part of the context, including the data sources from its Knowledge Base and provided instructions. A Run will add Messages to the Thread


# Quick Start

## Step 0: Initialize python client

```python
from agility import Agility

api_key = "your_agility_api_key"

client = Agility(api_key=api_key)
```

## Step 1: Create a Knowledge Base

```python
knowledge_base = client.knowledge_bases.create(
    name="Cleanlab docs",
    description="Developer-facing docs for using Cleanlab",
    ingestion_pipeline_params={
        "curate": {},
        "curate_document_store": {},
        "transform": {},
        "vector_store": {
            "weaviate_collection_name": "weaviate_collection_name"
        },
    },
)
```

## Step 2: Add a source to a Knowledge Base

```python
source = client.knowledge_bases.sources.create(
    knowledge_base_id=knowledge_base.id,
    name="Cleanlab docs URLs",
    description="APIs and tutorials for Studio and TLM",
    source_params={
        "urls": ["https://help.cleanlab.ai", "https://help.cleanlab.ai/tlm"]
    },
    source_schedule={
        "cron": "cron",
        "utc_offset": 0,
    },
)
```

## ?? Step x: figure out if there are any other necessary actions related to sources and documents, such as source syncing

## Step 3: Create an Assistant

```python
assistant = client.assistants.create(
    knowledge_base_id=knowledge_base.id,
    name="Chat with Cleanlab Docs",
    description="Chat with Cleanlab Docs for Studio and TLM",
)
```

## Step 4: Create a Thread

```python
thread = client.threads.create()
```

## Step 5: Add a Message to a Thread

```python
message = client.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to run TLM in batch-mode on a large number of datapoints. Can you help me?",
)
```

## Step 6: Create a Run

```python
run = client.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
```