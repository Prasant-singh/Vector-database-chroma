import chromadb

databasename="MyDatabase"
client = chromadb.PersistentClient(path=databasename)

#CREATE COLLECTION
collection_name = "MyCollection"
collection = client.get_or_create_collection(name=collection_name)
documents_to_add = [
    "The quick brown fox jumps over the lazy dog.",
    "Artificial intelligence is transforming industries worldwide.",
    "Quantum computing promises revolutionary advancements in data processing.",
    "The cat sat on the mat.",
    "Machine learning is a subset of AI.",
    "The dog chased the squirrel up the tree."
]

metadata = [
    {"source": "document1"},
    {"source": "document2"},
    {"source": "document3"},
    {"source": "document4"},
    {"source": "document5"},
    {"source": "document6"}
]

collection.add(
    documents=documents_to_add,
    metadatas=metadata,
    ids=["doc1", "doc2", "doc3", "doc4", "doc5", "doc6"]
)

query_text = "What is the quick brown fox doing?"
result=collection.query(
    query_texts=[query_text],
    n_results=3
)

for i in enumerate(result):
    print(f"Result {i[0]+1}:")
    print(f"  Document ID: {i[1]['ids'][0]}")
    print(f"  Content: {i[1]['documents'][0]}")
    print(f"  Metadata: {i[1]['metadatas'][0]}")
    print("-" * 20)