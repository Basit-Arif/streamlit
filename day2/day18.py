import numpy as np
import streamlit as st
from time import time 

import pandas as pd 

st.set_page_config(layout="wide")

with st.expander("About this app"):
    st.write("hello")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",width=250)
st.sidebar.header("Input")
username=st.sidebar.text_input("What your name ?")
age=st.sidebar.number_input("What your age?",placeholder="")
height=st.sidebar.number_input("What your height ?")
# st.sidebar.button()
st.header("output")
col1,col2,col3=st.columns(3)
with col1:
    if username!="":
        st.write(f"Your name is {username} ")
    else:
        st.write("enter your name")
with col2:
    if age!="":
        st.write(f"Your age is {age} ")
st.metric("temperature","80f",delta="1.2")

# progress=st.progress(0)
# for percent in range(100):
#     time.sleep(0.05)
#     progress.progress(percent+1,text="Operation is in process")

# st.balloons()
# progress.empty()
# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')

with st.form("my_form"):
    st.header("welcome to my_form")
    st.form_submit_button()
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)


st.header("2,Example of Form")
st.subheader("Coffee machine")
with st.form("my_form2"):
    st.header("Order your Coffee")
    coffee_been_value=st.selectbox("Select bean value",options=["arabian","turkish"])
    submitted=st.form_submit_button("Submit")
   
if submitted:
    st.markdown(
        f"""
        you have ordered {coffee_been_value}
        """
    )
with st.expander("About this app"):
    st.write("This app is about ordering coffee from different beans")
st.header("2. content of the st.expander")
st.write(st.experimental_get_query_params())
firstname = st.experimental_get_query_params()['firstname']
surname = st.experimental_get_query_params()['surname'][0]
st.write(f"hello{firstname}{surname}")

# day 24 st.chache
st.write("st.chache")

a0=time()
@st.cache_data
def load_data():
    df=pd.DataFrame(
        np.random.rand(2000000,5),
        columns=["a","b","c","d","e"]
    )
    return df
df=load_data()
st.write(load_data())
st.info(f'loading data took {time()-a0} seconds')

b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)

st.title("st.state")

def lbs_to_kg():
    st.session_state.kg=st.session_state.lbs/2.2046
def kg_to_kbs():
    st.session_state.lbs=st.session_state.kg*2.2045

pound=st.number_input("Pounts",key="lbs",on_change=lbs_to_kg)
kilogram=st.number_input("kg",key="kg",on_change=kg_to_kbs)
st.write("st.session_state object:", st.session_state["kg"])


