import streamlit as st
from rag import process_urls, generate_answer

st.title("Real Estate Research Assistant")
st.sidebar.header("Enter Real Estate News URLs:\n(at least one)")
url1 = st.sidebar.text_input("Enter the first URL")
url2 = st.sidebar.text_input("Enter the second URL")
url3 = st.sidebar.text_input("Enter the third URL")

placeholder = st.empty()

process_url_button = st.sidebar.button("Process URLs")
if process_url_button:
    urls = [url for url in (url1, url2, url3) if url!=""]
    if len(urls)==0:
        placeholder.info("You must enter at least one URL")
    else:
        for status in process_urls(urls):
            placeholder.info(status)
query = placeholder.text_input("Enter your query")
if query:
    try:
        answer, sources = generate_answer(query)
        st.header("Answer")
        st.write(answer)
        if sources:
            st.subheader("Sources")
            for source in sources:
                st.write(source)
    except RuntimeError as e:
        placeholder.text("You must process URLs first")
