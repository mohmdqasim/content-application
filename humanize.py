import streamlit as st
import requests
import json

def humanize_page():
    def humanize(text: str):
        url = "https://aitohumanconverter.com/v2/process.php"
        data = {'text': text}
        response = requests.post(url, data=data)
        # Decode the byte string to a regular string
        response_str = response.content.decode('utf-8')
        # Parse the JSON string to a dictionary
        response_dict = json.loads(response_str)
        # Extract the data
        status = response_dict['status']
        data = response_dict['data']
        return data

    st.title("Humanize Ai Content")

    st.header("Input")
        # Large text area for user to paste their code
    input_content = st.text_area("Your content here:", height=300)
    humanize = st.button("Humanize!")
    st.header("Output")
    if humanize:
        if input_content:
            st.markdown(humanize(input_content))
        else:
            st.info("Please add content")