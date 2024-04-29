# RAG vs GraphRAG

This notebook proposes the benefits of using a graph database for GraphRAG instead of the limited in-memory RAG approach.

To get started, load the contents of this repo into an ArangoGraph Jupyter notebook and be sure to update with your own OpenAI key.

Note: the gdelt dump is zipped within resources and needs unzipped for the notebook to work. The `unzip.py` script handles this for you.

## Upload to ArangoGraph

1. Upload the `Archive.zip` and `unzip.py` files in the same directory
2. Open a terminal and run `python unzip.py` within the above directory