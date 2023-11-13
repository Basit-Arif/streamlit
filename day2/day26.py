import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")

st.title("Board API APP")
st.sidebar.header("Input")
selected_type=st.sidebar.selectbox("Select an activity Type",["education","Recreational","social","div"])
suggested_activity_url=f'http://www.boredapi.com/api/activity?type={selected_type}'
suggested_activity=requests.get(suggested_activity_url).json()

col1,col2=st.columns(2)
with col1:
    with st.expander('About this App'):
        st.write("hello")
with col2:
    with st.expander('JSON Data'):
        st.write(suggested_activity)
        
st.header("Suggested Activity")
st.info("learn how to make website")
participants,activity,price=st.columns(3)
try:
    with participants:
        participants=st.metric("Number of Participants",value=suggested_activity["participants"])
    with activity:
        activity=st.metric("Type of activity",value=suggested_activity["type"])
    with price:
        price=st.metric("Price per person",value=suggested_activity["price"])

except Exception as e:
    st.write("this is not in data")
import json
import streamlit as st
from pathlib import Path

# As for Streamlit Elements, we will need all these objects.
# All available objects and there usage are listed there: https://github.com/okld/streamlit-elements#getting-started

import streamlit as st
from streamlit_shap import st_shap
import shap
from sklearn.model_selection import train_test_split
import xgboost
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

@st.experimental_memo
def load_data():
    return shap.datasets.adult()

@st.experimental_memo
def load_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    d_train = xgboost.DMatrix(X_train, label=y_train)
    d_test = xgboost.DMatrix(X_test, label=y_test)
    params = {
        "eta": 0.01,
        "objective": "binary:logistic",
        "subsample": 0.5,
        "base_score": np.mean(y_train),
        "eval_metric": "logloss",
        "n_jobs": -1,
    }
    model = xgboost.train(params, d_train, 10, evals = [(d_test, "test")], verbose_eval=100, early_stopping_rounds=20)
    return model

st.title("`streamlit-shap` for displaying SHAP plots in a Streamlit app")

with st.expander('About the app'):
    st.markdown('''[`streamlit-shap`](https://github.com/snehankekre/streamlit-shap) is a Streamlit component that provides a wrapper to display [SHAP](https://github.com/slundberg/shap) plots in [Streamlit](https://streamlit.io/). 
                    The library is developed by our in-house staff [Snehan Kekre](https://github.com/snehankekre) who also maintains the [Streamlit Documentation](https://docs.streamlit.io/) website.
                ''')

st.header('Input data')
X,y = load_data()
X_display,y_display = shap.datasets.adult(display=True)

with st.expander('About the data'):
    st.write('Adult census data is used as the example dataset.')
with st.expander('X'):
    st.dataframe(X)
with st.expander('y'):
    st.dataframe(y)

st.header('SHAP output')

# train XGBoost model
model = load_model(X, y)

# compute SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

with st.expander('Waterfall plot'):
    st_shap(shap.plots.waterfall(shap_values[0]), height=300)
with st.expander('Beeswarm plot'):
    st_shap(shap.plots.beeswarm(shap_values), height=300)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

with st.expander('Force plot'):
    st.subheader('First data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:]), height=200, width=1000)
    st.subheader('First thousand data instance')
    st_shap(shap.force_plot(explainer.expected_value, shap_values[:1000,:], X_display.iloc[:1000,:]), height=400, width=1000)