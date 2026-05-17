import streamlit as st
from utils.pdf_handler import extract_text_from_pdf, split_text
from utils.vector_store import create_vector_store
from utils.chatbot import ask_gemini

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📘",
    layout="wide"
)

st.title("📘 AI Research Assistant")
st.caption("Upload a PDF and ask questions from it using AI.")

# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "retrieved_docs" not in st.session_state:
    st.session_state.retrieved_docs = None


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("Upload PDF")

    uploaded_pdf = st.file_uploader("Choose a PDF file", type="pdf")

    if st.button("Remove PDF"):
        st.session_state.vector_store = None
        st.session_state.chat_history = []
        st.session_state.retrieved_docs = None
        st.rerun()


# ---------------- PROCESS PDF ----------------
if uploaded_pdf is not None and st.session_state.vector_store is None:

    with st.spinner("Processing PDF..."):

        raw_text = extract_text_from_pdf(uploaded_pdf)
        text_chunks = split_text(raw_text)
        vector_store = create_vector_store(text_chunks)

        st.session_state.vector_store = vector_store

    st.success("PDF processed successfully!")


# ---------------- CHAT SECTION ----------------
if st.session_state.vector_store is not None:

    user_question = st.chat_input("Ask a question from the PDF")

    if user_question:

        # store user message
        st.session_state.chat_history.append({
            "role": "user",
            "message": user_question
        })

        # retrieve docs
        docs = st.session_state.vector_store.similarity_search_with_score(
            user_question,
            k=5
        )

        docs = sorted(docs, key=lambda x: x[1])

        context = "\n".join([doc[0].page_content for doc in docs[:3]])

        # generate answer
        with st.spinner("Generating answer..."):
            answer = ask_gemini(user_question, context)

        # store assistant message
        st.session_state.chat_history.append({
            "role": "assistant",
            "message": answer
        })

        st.session_state.retrieved_docs = docs

    # ---------------- RENDER CHAT HISTORY ----------------
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.write(chat["message"])

    # ---------------- RETRIEVED CONTEXT ----------------
    if st.session_state.retrieved_docs is not None:

        with st.expander("Retrieved Context"):

            for i, (doc, score) in enumerate(st.session_state.retrieved_docs):

                st.markdown(f"### Retrieved Chunk {i+1}")
                st.code(doc.page_content[:300])

else:
    st.info("Please upload a PDF file to begin.")