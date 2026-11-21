from langchain_openai import OpenAIEmbeddings

# Vector Embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
)