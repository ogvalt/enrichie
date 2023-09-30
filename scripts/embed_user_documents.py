
def retrieve_documents():
    """
    Retrieve them from path?
    """
    ...

def get_embeddings():
    """
    parametrize by model ?
    """
    ...

def store_embeddings():
    """
    store document-embeddings pairs?
    """
    ...

def main():
    docs = retrieve_documents()
    embeddings = get_embeddings()
    store_embeddings()


if __name__ == "__main__":
    main()