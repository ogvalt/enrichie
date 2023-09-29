# Enrichie

The idea is to build system where ChatGPT answers questions based on the information provided by user.

## Development

1. For local development I'm going to use [milvus-lite](https://github.com/milvus-io/milvus-lite). For production it's better use Standalone Milvus (located in [docker-compose.yaml](./docker-compose.yml))

## Plans

1. Retrieve embeddings for collection of documents and store them in vector database.
2. Terminal application that will answer my question about the documents stored in vector database.

## Technologies

1. Vector DB: https://milvus.io/
