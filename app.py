import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="AI Text Summarizer")

st.title("AI Text Summarizer")

input_text = st.text_area(
    "Paste your text here:",
    height=250
)

max_words = st.slider(
    "Maximum summary length (words)",
    min_value=50,
    max_value=200,
    value=120
)

if st.button("Summarize"):
    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize_text(input_text, max_words)
            st.subheader("Summary")
            st.write(summary)
