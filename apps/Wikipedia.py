import streamlit as st
import random
import time
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
import time
from langchain_core.pydantic_v1 import BaseModel, Field

def wiki():
    api_wrapper = WikipediaAPIWrapper(top_k_results=3, doc_content_chars_max=1000)
    class WikiInputs(BaseModel):
        query: str = Field(
            description="query to look up in Wikipedia"
        )
    tool = WikipediaQueryRun(
        name="wiki-tool",
        description="look up things in wikipedia",
        args_schema=WikiInputs,
        api_wrapper=api_wrapper,
        return_direct=True,
    )

    def stream_data(query):
        result = tool.run(query)
        for word in result.split(" "):
            yield word + " "
            time.sleep(0.02)

    st.title("Ask from Wikipedia!!")
    with st.sidebar:
        st.write("Code Link")
        st.markdown("[![Github](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/mohmdqasim/chat-with-wikipedia-without-any-api)")
        st.markdown("<br>",unsafe_allow_html=True)
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(stream_data(prompt))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})