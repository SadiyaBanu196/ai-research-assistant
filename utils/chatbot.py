import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(question, context):
    prompt = f"""
    You are an AI Research Assistant.

    Answer using the provided context.

    Rules:
    - Keep responses concise and structured.
    - Use bullet points when appropriate.
    - For summaries:
        - identify the main topic
        - explain key points briefly
        - avoid repetition
    - Make reasonable inferences only from context.
    - Do not invent information.
    - If information is unavailable, say:
    "I could not find that information in the PDF."

    Context:
    {context}

    Question:
    {question}
    """
    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"