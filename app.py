
import streamlit as st
from agent.assistant import answer_question

st.set_page_config(
    page_title="SupportPilot AI",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 SupportPilot AI")
st.caption("AI-powered customer support assistant")

st.info(
    "Ask questions about login, password reset, "
    "account security, or application troubleshooting."
)

# Store conversation messages for the current session.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("status"):
            st.caption(f"Status: {message['status']}")

        if message.get("sources"):
            with st.expander("View supporting documentation"):
                for source in message["sources"]:
                    st.write(source)

# Accept a new question.
question = st.chat_input("Type your support question...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question,
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Checking support information..."):
            result = answer_question(question)

        st.markdown(result["answer"])
        st.caption(f"Status: {result['status']}")

        if result["sources"]:
            with st.expander("View supporting documentation"):
                for source in result["sources"]:
                    st.write(source)

    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"],
        "status": result["status"],
        "sources": result["sources"],
    })
