import streamlit as st
import openai
import time

st.set_page_config(page_title="LLM Question Answering 🤖✨", page_icon="✨")

st.title("Discover with LLM: Your Questions, Answered! 🌟")

# Initialize session_state
if 'validated' not in st.session_state:
    st.session_state.validated = False

key = st.sidebar.text_input("Enter your OpenAI API Key", placeholder="Enter your OpenAI API Key", type="password")

@st.cache_resource()
def initialize_openai():
    return openai

def validate_api_key(key):
    openai_instance = initialize_openai()
    openai_instance.api_key = key
    try:
        openai_instance.Completion.create(model="text-davinci-003", prompt="Hello", max_tokens=5)
        return True
    except openai.error.AuthenticationError:
        st.error("Invalid API Key")
        return False

def ask_question(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

if key == "":
    st.warning("Please enter your OpenAI API Key")
else:
    if not st.session_state.validated:
        st.session_state.validated = validate_api_key(key)
        if st.session_state.validated:
            st.success("API Key is valid")

question = st.text_input("Enter your Question")

ask_button_label = "Ask Question" if st.session_state.validated else "Enter a valid API Key"

if st.button(ask_button_label, key="ask_button"):
    if st.session_state.validated:
        try:
            response = ask_question(prompt=question)
            st.write("LLM's Response:")
            st.info(response)
        except openai.error.AuthenticationError:
            st.error("Enter a valid API Key")
        except openai.error.APIError as e:
            if "Rate limit reached" in str(e):
                st.error("Rate limit reached. Please wait and try again.")
                time.sleep(20)  # Wait for 20 seconds before retrying
                try:
                    response = ask_question(prompt=question)
                    st.write("LLM's Response:")
                    st.info(response)
                except openai.error.APIError as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a valid API Key to proceed")
