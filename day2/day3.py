import streamlit as st
import altair as alt 
import pandas  as pd 
import numpy as  np
from datetime import time,date
from PIL import Image

# add_side_bar=st.sidebar.selectbox("Aggregatebox",("individual","aggregate"))
# if add_side_bar=="individual":
#     st.metric(label="item Sold",value=10,delta=-10)    
# if add_side_bar=="aggregate":
#     st.metric(label="item Sold",value=20,delta=100)

st.sidebar.selectbox("choose youtube",("channel","hi"))
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(x="a",y="b",size="c",color="c")
st.write(c)
data=pd.DataFrame({
    "first_columns":[1,3,4,5],
    "second_column":[6,7,8,9],
    "film_name":["kahbhi khushi","khabhi ghum","taray zameen par","dukh"]
    })
st.slider("how old are you",min_value=0,max_value=80,step=10)
list=tuple(data["film_name"])

movie_name=st.selectbox("select movie",list)
st.write("the movie name "+movie_name)


st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
appointmenet=st.slider("your schedule time",value=(time(11,30),time(12,30)))
st.write(f"your schedule appointmenet {appointmenet}")
start=st.slider("when did you start",value=date(2022,12,20),format="DD/MM/YY")
st.write(f"you started on  {start}")

data2=pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"])
st.line_chart(data2)

options=st.multiselect("which options",["green","yellow","red"],["green","red"])
st.write(options)

icecreame=st.radio("what do you want", options=["Icecreame","coffe","cola"])


if icecreame:
    st.write("here is your " + icecreame)

import ydata_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')



st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.write(st.secrets["this_var"])


uploader=st.file_uploader("upload file",type="csv")
if uploader is not None:
    
    data=pd.read_csv(uploader)
    st.subheader("data reader")
    st.table(data[:10])
    st.write(data.describe())

    
else :
    st.info("no file selected")

    