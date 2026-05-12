import streamlit as st
from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pypdf import PdfReader

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant"
)

st.set_page_config(page_title="Personal AI Chatbot", page_icon="🐋")

st.title("Personal Chatbot")
st.caption("Using LangChain ,Groq LLMs and Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

with st.sidebar:
    st.header("Upload Document")

    uploaded_file = st.file_uploader(
        "Upload a PDF or TXT file",
        type=["pdf", "txt"]
    )

    if uploaded_file:
        document_text = ""

        if uploaded_file.type == "application/pdf":
            pdf_reader = PdfReader(uploaded_file)

            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    document_text += text + "\n"

        elif uploaded_file.type == "text/plain":
            document_text = uploaded_file.read().decode("utf-8")

        st.session_state.document_text = document_text

        st.success("Document uploaded successfully!")

        if st.button("Generate Summary"):
            summary_prompt = ChatPromptTemplate.from_template(
                """
                You are an AI assistant.

                Summarize the following document clearly and concisely.

                Document:
                {document}
                """
            )

            summary_chain = summary_prompt | llm

            summary_response = summary_chain.invoke({
                "document": st.session_state.document_text[:12000]
            })

            st.subheader("Document Summary")
            st.write(summary_response.content)

user_input = st.chat_input("Ask something...")

if user_input:

    st.session_state.messages.append(("You", user_input))

    if st.session_state.document_text:

        prompt = ChatPromptTemplate.from_template(
            """
            You are a helpful personal AI assistant.

            Use the uploaded document to answer the user's question.

            Document:
            {document}

            User Question:
            {question}
            """
        )

        chain = prompt | llm

        response = chain.invoke({
            "document": st.session_state.document_text[:12000],
            "question": user_input
        })

    else:

        prompt = ChatPromptTemplate.from_template(
            """
            You are a helpful personal AI chatbot.

            User Question:
            {question}
            """
        )

        chain = prompt | llm

        response = chain.invoke({
            "question": user_input
        })

    st.session_state.messages.append(("Bot", response.content))

for sender, message in st.session_state.messages:
    with st.chat_message(sender):
        st.write(message)