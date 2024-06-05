import streamlit as st
import requests
import json

# Function to generate response from AskLLama model
def generate_response(prompt):
    url = "http://host.docker.internal:11434/api/generate"
    headers = {'Content-Type': 'application/json'}
    history = []
    
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "AskLLama",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        return "ERROR: " + response.text

# Streamlit UI
st.set_page_config(page_title="Ask LLaMA", layout='centered', initial_sidebar_state='collapsed')
st.header("ASK LLaMA 🤖")

input_text = st.text_input("Enter the topic you want me to explain")

# Creating two more columns for additional two fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No. of Words')

with col2:
    blog_style = st.selectbox('Writing the explanation for', ('Common People', 'Researchers', 'Data Scientist'), index=0)

submit = st.button("Generate")

# Display response
if submit:
    new_input_text = input_text + " in " + no_words + " words for " + blog_style
    response = generate_response(new_input_text)
    st.write(response)