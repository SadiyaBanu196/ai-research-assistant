from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def create_vector_store(text_chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # FIX: ensure chunks are valid strings
    text_chunks = [str(chunk) for chunk in text_chunks]

    vector_store = FAISS.from_texts(
        texts=text_chunks,
        embedding=embeddings
    )

    return vector_store