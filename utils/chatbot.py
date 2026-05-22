import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(question, context):
    prompt = f"""
    You are a helpful AI assistant for a PDF document.

    Answer using the provided context.

    Rules:
    - If the user greets (hi, hello, hey), respond politely and briefly.
    - Keep responses concise and structured.
    - Use bullet points when appropriate.
    - For summaries:
        - identify the main topic
        - explain key points briefly
        - avoid repetition
    - Make reasonable inferences only from context.
    - Do not invent information.
    - If information is unavailable, say:
    "This question is outside the PDF content. Please ask something from the document."

    Important:
    - Do NOT repeat the same greeting every time.
    - Keep responses short and human-like.
    - Avoid sounding robotic.

    
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